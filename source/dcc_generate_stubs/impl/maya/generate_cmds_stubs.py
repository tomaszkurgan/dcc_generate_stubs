import itertools
import os
import re
import operator
import textwrap
from collections import OrderedDict

import requests
import bs4
from bs4 import BeautifulSoup
from urlparse import urljoin

from .. import utils
from ... import config

DESC, FLAG, SHORT_NAME, FLAG_DESC, DOC_LINK, EXAMPLE = (1 << i for i in range(6))
ALL_FEATURES = DESC | FLAG | SHORT_NAME | FLAG_DESC | DOC_LINK | EXAMPLE


def get_commands(url):
    """Returns relative links to all commands"""
    with requests.Session() as session:
        response = session.get(url)

        # get frame links
        soup = BeautifulSoup(response.text, 'html.parser')
        content_frame = soup.find_all('frame', {'name': 'contentFrame'})[0]

        content_frame_url = urljoin(url, content_frame.get('src'))
        response = session.get(content_frame_url, headers={'Referer': url})
        soup = BeautifulSoup(response.text, 'html.parser')

    return [a.get('href') for a in soup.select('table a')]


def get_command_properties(document):
    """Looking for <cmd> is (NOT) undoable, (NOT) queryable, and (NOT) editable."""
    anchor = document.find('p', {'id': 'synopsis'})  # type: bs4.element.Tag
    if not anchor:
        return {}

    property_line = anchor.next_sibling.next_sibling.text
    property_line = utils.strip_empty_lines(property_line)

    properties = {}
    for property_name in ('undoable', 'queryable', 'editable'):
        match = re.search(r'(?:NOT)? %s' % property_name, property_line)
        properties[property_name] = 'NOT' not in match.group() if match else False
    return properties


def find_parameters_table(document):
    anchor = document.find('th', text='Long name (short name)')  # type: bs4.element.Tag
    if not anchor:
        return None
    while anchor.parent:
        anchor = anchor.parent
        if anchor.name == 'table':
            return anchor
    return None


def chunk_flags_table(table):
    all_rows = table.find_all('tr', recursive=False)
    for index in range(len(all_rows)):
        if all_rows[index].get('bgcolor', '') == '#EEEEEE':
            yield all_rows[index], all_rows[index + 1]


def parse_flag_name(flag_name):
    match = re.match(r'^(?P<longname>.*?)(\((?P<shortname>.*)\))?$', flag_name)
    if match:
        return match.group('longname'), match.group('shortname') or ''
    return flag_name, ''


def get_command_flags(document, command_properties=None):
    def create_flag_item(flag_short_name, flag_type, flag_properties=(), flag_desc=''):
        return {
            'short_name': flag_short_name,
            'type': flag_type,
            'properties': flag_properties,
            'desc': flag_desc,
        }

    command_properties = command_properties or {}

    parameters = OrderedDict()
    if command_properties.get('queryable', False):
        parameters['query'] = create_flag_item('q', 'boolean')
        parameters['q'] = create_flag_item('', 'boolean')
    if command_properties.get('editable', False):
        parameters['edit'] = create_flag_item('e', 'boolean')
        parameters['e'] = create_flag_item('', 'boolean')

    table = find_parameters_table(document)
    if not table:
        return parameters

    for name_row, desc_row in chunk_flags_table(table):
        name_item, type_item, properties_item = name_row.find_all('td', recursive=False)

        flag_name, flag_short_name = parse_flag_name(name_item.find('code').text.strip())

        flag_type = type_item.find('code').text.strip()

        flag_properties = [os.path.splitext(os.path.basename(img_tag['src']))[0][0].upper()
                           for img_tag in properties_item.find_all('img')]

        flag_desc = ' '.join([line.strip() for line in desc_row.find_all('td')[-1].text.splitlines()])

        parameters[flag_name] = create_flag_item(flag_short_name, flag_type, flag_properties, flag_desc)

    return parameters


def get_command_examples(document):
    """
    Args:
        document (BeautifulSoup):
    """
    anchor = document.find('a', {'name': 'hExamples'})  # type: bs4.element.Tag
    if not anchor:
        return ''
    anchor = anchor.parent  # type: bs4.element.Tag

    example = anchor.next_sibling.text
    example = utils.strip_empty_lines(example)
    example = ''.join(line.replace('"""', "'''") for line in example.splitlines(True))

    return example


def compose_python_function_def(command_name, command_properties, command_flags,
                                documentation_link=None,
                                command_example=None,
                                feature_mask=None):
    if feature_mask is None:
        param_feature_mapping = zip((command_flags, documentation_link, command_example), (FLAG, DOC_LINK, EXAMPLE))
        feature_mask = feature_mask or reduce(
            operator.and_, [~feature for param, feature in param_feature_mapping if param is None], ALL_FEATURES
        )

    command_parameters_short_names = filter(
        None,
        (command_flags[command_name]['short_name'] for command_name in command_flags.iterkeys())
    ) if feature_mask & SHORT_NAME else []

    command_parameters_repr = ', '.join(
        utils.deduplicate(
            itertools.chain(
                command_flags.iterkeys(),
                command_parameters_short_names
            )
        )
    )

    description_repr = ''
    if feature_mask & DESC:
        description_repr = '%s is %s' % (command_name,
                                         ('NOT ' if command_properties.get('undoable', False) else '') + 'undoable')

    flags_repr = None
    if feature_mask & FLAG:
        flags_list = []
        for flag_name, flag_spec in command_flags.iteritems():
            if feature_mask & FLAG_DESC:
                try:
                    desc = str(flag_spec['desc']).strip()
                except UnicodeEncodeError:
                    desc = ''
            else:
                desc = ''

            short_name = ''
            if feature_mask & SHORT_NAME:
                short_name = '(-%s)' % flag_spec['short_name'] if flag_spec['short_name'] else ''

            flags_list.append(
                '{name} ({type}): {short_name} {prop} {desc}'.format(
                    name=flag_name,
                    type=flag_spec['type'],
                    short_name=short_name,
                    prop='<%s>' % ' '.join(flag_spec['properties']) if flag_spec['properties'] else '',
                    desc=desc)
            )

        flags_repr = utils.format_string(utils.dedent_string('''
            Args:
                {args}
        '''), args='\n'.join(flags_list))

    documentation_link_repr = None
    if feature_mask & DOC_LINK:
        documentation_link_repr = utils.format_string(utils.dedent_string('''
            Documentation:
                {documentation_link}
        '''), documentation_link=documentation_link)

    example_repr = None
    if feature_mask & EXAMPLE:
        example_repr = utils.format_string(utils.dedent_string('''
            Examples:
                {example}
        '''), example=''.join(['- %s' % line for line in command_example.splitlines(True)]))

    function_def = utils.format_string(
        utils.dedent_string('''
        def {function_name}({function_parameters}):
            """
            {description}
            
            {flags}
            {doc_link}
            {example}
            """
        '''),
        function_name=command_name,
        function_parameters=textwrap.fill(command_parameters_repr, 80),
        description=description_repr or utils.EMPTY_FORMATTING,
        flags=flags_repr or utils.EMPTY_FORMATTING,
        doc_link=documentation_link_repr or utils.EMPTY_FORMATTING,
        example=example_repr or utils.EMPTY_FORMATTING,
    )

    return function_def


def generate_stubs(output_file_path=None, force_override=False,
                   cmds_url=None, maya_version=None,
                   limit=None,
                   feature_mask=ALL_FEATURES):
    if not cmds_url and not maya_version:
        raise ValueError('One of the arguments cmds_url, maya_version is required')

    if maya_version:
        try:
            cmds_url = config.DEFAULT_CMDS_URL[maya_version]
        except KeyError:
            raise KeyError('Unknown Maya version. Valid versions are: %s' % ', '.join(config.DEFAULT_CMDS_URL.keys()))

    if output_file_path:
        output_file_path = os.path.realpath(output_file_path)

        if not force_override:
            if not utils.file_exists_prompt(output_file_path):
                return

        utils.clear_file_content(output_file_path)

        def write_output(content):
            with open(output_file_path, 'a') as f:
                f.write(content + '\n\n')
    else:
        def write_output(content):
            print content + '\n'

    commands = get_commands(cmds_url)

    write_output(utils.get_preamble())

    for p, command in utils.percentage(commands[:limit]):
        cmd_url = urljoin(cmds_url, command)

        print '# Processing [%6.2f%%] %s...' % (p, command)

        command_name, _ = os.path.splitext(command)

        response = requests.get(cmd_url)
        document = BeautifulSoup(response.text, 'html.parser')

        command_properties = get_command_properties(document)
        command_flags = get_command_flags(document, command_properties)
        command_documentation_link = cmd_url if (feature_mask & DOC_LINK) else None
        command_example = get_command_examples(document) if (feature_mask & EXAMPLE) else None

        py_fun_def = compose_python_function_def(command_name,
                                                 command_properties,
                                                 command_flags,
                                                 documentation_link=command_documentation_link,
                                                 command_example=command_example,
                                                 feature_mask=feature_mask)
        write_output(py_fun_def)
