import sys
import operator
import argparse

from . import config

from dcc_generate_stubs.impl.maya import generate_cmds_stubs

if __name__ == '__main__':
    main_parser = argparse.ArgumentParser(
        prog='dcc_generate_stubs',
        description='Generates stubs for every-day DCC development.'
    )

    main_subparsers = main_parser.add_subparsers(dest='dcc')

    maya_parser = main_subparsers.add_parser(
        'maya',
        help='Maya APIs stubs generator.'
    )

    maya_subparsers = maya_parser.add_subparsers(dest='api')

    cmds_parser = maya_subparsers.add_parser(
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

    cmds_parser.add_argument('-s', '--skip', dest='feature_mask', action='append', default=[],
                             choices=['desc', 'flag', 'short_name', 'flag_desc', 'doc_link', 'example'])

    args = vars(main_parser.parse_args())
    dcc = args.pop('dcc')
    api = args.pop('api', None)

    if dcc == 'maya':
        if api == 'cmds':
            try:
                args['feature_mask'] = generate_cmds_stubs.ALL_FEATURES & ~reduce(
                    operator.or_, [getattr(generate_cmds_stubs, feature.upper()) for feature in args['feature_mask']], 0
                )
                generate_cmds_stubs.generate_stubs(**args)
            except KeyboardInterrupt:
                sys.exit(0)
