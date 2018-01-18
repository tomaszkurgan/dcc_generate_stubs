import re
import os
import string
import textwrap

import errno


def file_exists_prompt(path):
    if not os.path.exists(path):
        return True

    override = raw_input('File %s already exists. Override? (y/n) [n]:' % path)
    if override in ['y', 'Y', 'yes']:
        return True
    return False


def clear_file_content(path, skip_non_existsing=True):
    try:
        open(path, 'w').close()
    except IOError as e:
        if e.errno == errno.ENOENT:
            return
        raise


class Formatter(string.Formatter):
    _CHARACTERS_IN_LINE_RE = re.compile(r'[^\n\r]*$')
    _NEW_LINE_RE = re.compile(r'[\n\r]')

    def __init__(self):
        super(Formatter, self).__init__()
        self.adjust_indent = True

    def _vformat(self, format_string, args, kwargs, used_args, recursion_depth):
        if recursion_depth < 0:
            raise ValueError('Max string recursion exceeded')

        result = []
        for literal_text, field_name, format_spec, conversion in self.parse(format_string):
            if literal_text:
                result.append(literal_text)

            if field_name is not None:
                obj, arg_used = self.get_field(field_name, args, kwargs)
                obj, arg_used, type(obj), type(arg_used)
                used_args.add(arg_used)

                obj = self.convert_field(obj, conversion)

                format_spec = self._vformat(format_spec, args, kwargs, used_args, recursion_depth - 1)

                # format the object and append to the result
                if self.adjust_indent and literal_text:
                    current_line_tokens = []
                    for token in reversed(result):
                        current_line_tokens.append(token)
                        if self._NEW_LINE_RE.search(token):
                            break
                    indent = ' ' * len(self._CHARACTERS_IN_LINE_RE.search(''.join(current_line_tokens)).group())
                    obj = ''.join([indent + line if i else line for i, line in enumerate(obj.splitlines(True))])

                result.append(self.format_field(obj, format_spec))

        return ''.join(result)


def format_string(s, *args, **kwargs):
    formatter = Formatter()
    return formatter.format(s, *args, **kwargs)


def dedent_string(s):
    return textwrap.dedent(s).strip()


def percentage(collection):
    collection_len = float(len(collection))
    for i, item in enumerate(collection):
        percent = ((float(i + 1) * 100) / collection_len)
        yield percent, item


def strip_empty_lines(s):
    lines = s.splitlines()
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()
    return '\n'.join(lines)
