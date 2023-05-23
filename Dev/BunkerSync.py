from Synchronizer import Synchronizer
import argparse
import config

def main():

    parser = argparse.ArgumentParser(
        description='Welcome to BunkerSync tool!')

    # parser.add_argument('-p', '--publish', action='store_true',
    #                     help='Option to publish a given branch from internal repository to external repository.')
    # parser.add_argument('-f', '--fetch', action='store_true',
    #                     help='Option to fetch all new branches with a given prefix from external repository to the internal repository.')
    parser.add_argument('-s', '--src', action='store',
                        default=None,  type=str, help='source repository url.')
    parser.add_argument('-d', '--dst', action='store',
                        default=None, type=str, help='destination repository url.')
    # parser.add_argument('-@', '--prefix', default=None, action='store', type=str,
    #                     help='(Required when -f is on) Prefix of external branches to be pulled to internal repository.')
    parser.add_argument('-fm', '--filter_map', default=None, action='store', type=str,
                        help='Path of the filtering map that includes files or folders names to be filtered.')
    parser.add_argument('-sb', '--src_branch', default=None, type=str,
                        help='The name of the branch in the source repository.')
    parser.add_argument('-db', '--dst_branch', default=None, type=str,
                        help='The name of the branch in the destination repository.')
    parser.add_argument('-bb', '--base_branch', default=None, type=str,
                        help='The base branch name to be the base of the new fetched branch.')

    args = parser.parse_args()

    def check_urls():
        if args.src is None:
            parser.error(
                'Source repository url should be specified as the following: --src=<url> or -s=<url>')
        if args.dst is None:
            parser.error(
                'Destination repository url should be specified as the following: --dst=<url> or -d=<url>')

    check_urls()
    Synchronizer().sync(src_url=args.src,
                        dst_url=args.dst,
                        src_branch_name=args.src_branch,
                        dst_branch_name=args.dst_branch,
                        base_branch=args.base_branch,
                        filter_path=args.filter_map)


    # if args.publish:
    #     check_urls()
    #     if args.internal_branch is None:
    #         parser.error(
    #             'internal_branch argument is required when using -p/--publish.')
    #     if args.internal_branch is None:
    #         args.internal_branch = args.external_branch
    #     if args.branch_base is None:
    #         args.branch_base = config.external_default_branch
    #     Synchronizer().sync_internal_external(
    #         src_repo_url=args.internal,
    #         dst_repo_url=args.external,
    #         internal_branch_name=args.internal_branch,
    #         external_branch_name=args.external_branch,
    #         external_branch_base = args.branch_base,
    #         filter_map_path=args.filter_map)

    # elif args.fetch:
    #     check_urls()
    #     prefix_fetch = not (args.prefix is None)
    #     branch_fetch = not ((args.internal_branch is None)) or not (
    #         (args.external_branch is None)) or not ((args.branch_base is None))

    #     if prefix_fetch:
    #         if args.branch_base is None:
    #             args.branch_base = config.internal_default_branch

    #         Synchronizer().sync_external_internal_with_prefix(
    #             internal_repo_url=args.internal,
    #             external_repo_url=args.external,
    #             prefix=args.prefix,
    #             fetch_base=args.branch_base
    #         )   
    #     elif branch_fetch:
    #         if args.external_branch is None:
    #             parser.error(
    #                 'external_branch argument is required when using -f/--fetch.')            
    #         if args.internal_branch is None:
    #             args.internal_branch = args.external_branch

    #         if args.branch_base is None:
    #             args.branch_base = config.internal_default_branch

    #         Synchronizer().sync_external_internal_with_branch(
    #             internal_repo_url=args.internal,
    #             external_repo_url=args.external,
    #             dst_branch_name=args.external_branch,
    #             src_branch_name=args.internal_branch,
    #             src_branch_base=args.branch_base
    #         )
                
    #     else:
    #         parser.error(
    #             'When using -f/--fetch, one of two following cases is required (1) --prefix \n (2) --internal_branch, --external_branch and --branch_base')

    # else:
    print(get_logo())
    parser.print_help()


def get_logo():
    logo = r'''


                *-+-+-+-+-+-+-+-+-+-+-+*
                |         .--.         |
                |        / {} \        |
                |_______/  /\  \_______|
                |#######| |  | |#######|
                |#######`-'++'-´#######|
                *-+-+-+BunkerSync+-+-+-*
                
                Author: Luai Okasha
                E-mail: Luaiokasha@gmail.com
                Github: https://github.com/okashaluai/BunkerSync.git
    
    '''

    return logo


if __name__ == "__main__":
    main()
