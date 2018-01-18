import os
import re
import textwrap
from collections import OrderedDict

import requests
import bs4
from bs4 import BeautifulSoup
from urlparse import urljoin

from . import utils
from . import config


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
        return match.group('longname'), match.group('longname') or ''
    return flag_name, ''


def get_command_flags(document):
    """
    Args:
        document (BeautifulSoup):
    """
    parameters = OrderedDict()
    table = find_parameters_table(document)
    if not table:
        return parameters

    for name_row, desc_row in chunk_flags_table(table):
        name_item, type_item, properties_item = name_row.find_all('td', recursive=False)

        flag_name, flag_short_name = parse_flag_name(name_item.find('code').text.strip())

        flag_type = type_item.find('code').text.strip()

        flag_properties = [os.path.splitext(os.path.basename(img_tag['src']))[0]
                           for img_tag in properties_item.find_all('img')]

        flag_desc = ' '.join([line.strip() for line in desc_row.find_all('td')[-1].text.splitlines()])

        parameters[flag_name] = {
            'short_name': flag_short_name,
            'type': flag_type,
            'properties': flag_properties,
            'desc': flag_desc,
        }

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


def compose_python_function_def(command_name, command_flags, documentation_link, command_example=None):
    command_example = command_example or ''

    arg_list = []
    for flag_name, flag_spec in command_flags.iteritems():
        try:
            desc = str(flag_spec['desc'])
        except UnicodeEncodeError:
            desc = 'Inaccessible'
        arg_list.append(
            '{name}({type}): {desc}'.format(name=flag_name, type=flag_spec['type'], desc=desc)
        )
    args = '\n'.join(arg_list)

    function_def = utils.format_string(
        utils.dedent_string('''
        def {function_name}({function_parameters}):
            """
            {description}
            Args:
                {args}
                
            Documentation:
                {documentation_link}
                
            Examples:
                {example}
            """
        '''),
        function_name=command_name,
        function_parameters=textwrap.fill(', '.join(command_flags.keys()), 80),
        description='',
        args=args,
        documentation_link=documentation_link,
        example=''.join(['- %s' % line for line in command_example.splitlines(True)])
    )

    return function_def


def generate_stubs(output_file_path=None, force_override=False, cmds_url=None, maya_version=None, limit=None):
    if not cmds_url and not maya_version:
        raise ValueError('One of the arguments cmds_url, maya_version is required')

    if maya_version:
        try:
            cmds_url = config.DEFAULT_CMDS_URL[maya_version]
        except KeyError:
            raise KeyError('Unknown Maya version. Valid versions are: %s' % ', '.join(config.DEFAULT_CMDS_URL.keys()))

    if output_file_path and not force_override:
        if not utils.file_exists_prompt(output_file_path):
            return

    commands = get_commands(cmds_url)

    if output_file_path:
        utils.clear_file_content(output_file_path)

    for p, command in utils.percentage(commands[:limit]):
        cmd_url = urljoin(cmds_url, command)

        print 'Processing [%6.2f%%] %s...' % (p, command)

        command_name, _ = os.path.splitext(command)

        response = requests.get(cmd_url)
        document = BeautifulSoup(response.text, 'html.parser')

        command_flags = get_command_flags(document)
        command_example = get_command_examples(document)

        py_fun_def = compose_python_function_def(command_name, command_flags, cmd_url, command_example=command_example)

        if output_file_path:
            with open(output_file_path, 'a') as f:
                f.write(py_fun_def + '\n')
        else:
            print py_fun_def + '\n'
