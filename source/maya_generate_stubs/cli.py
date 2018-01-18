import argparse

import sys

from .impl import config

from maya_generate_stubs.impl import generate_cmds_stubs

if __name__ == '__main__':
    main_parser = argparse.ArgumentParser(
        prog='Maya - Generate Stubs',
        description='Generates stubs for every-day Maya development.'
    )

    subparsers = main_parser.add_subparsers()

    cmds_parser = subparsers.add_parser(
        'cmds',
        help='Maya.cmds stubs generator.'
    )
    cmds_parser.add_argument('-o', '--output', dest='output_file_path')
    cmds_parser.add_argument('-w', '--override', dest='force_override', action='store_true')

    source = cmds_parser.add_mutually_exclusive_group(required=True)
    source.add_argument('-v', '--version', dest='maya_version',
                        choices=config.DEFAULT_CMDS_URL.keys(), help='Exclusive to -url.')
    source.add_argument('-u', '--url', dest='cmds_url', help='Exclusive to -version.')

    cmds_parser.add_argument('-l', '--limit', dest='limit', type=int,
                        help='[Debugging option] - limit the number of processed commands')

    args = main_parser.parse_args()
    try:
        generate_cmds_stubs.generate_stubs(**vars(args))
    except KeyboardInterrupt:
        sys.exit(0)
