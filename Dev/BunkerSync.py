from Synchronizer import Synchronizer
import sys
import utils
import argparse

def main():
	
    parser = argparse.ArgumentParser(
        description =   'Welcome to BunkerSync tool!')
    
    
    parser.add_argument('-p', '--publish', action='store_true')
    parser.add_argument('-f', '--fetch', action='store_true')
    parser.add_argument('-i', '--internal',action='store',default=None,  type = str, help = 'Internal repository url.')
    parser.add_argument('-e', '--external',action='store', default=None, type = str, help = 'External repository url.')
    parser.add_argument('-b', '--branch', metavar='branch',default= None, action='store', type = str, help = '(Required when -p is on) Name of internal branch to be published to external repository.')
    parser.add_argument('-@', '--prefix', metavar = 'prefix',default= None, action='store', type = str, help = '(Required when -f is on) Prefix of external branches to be pulled to internal repository.')
    parser.add_argument('-fm', '--filter_map', metavar = 'filter_map_path',default= None, action='store', type=str, help = 'Path of the filtering map that includes files or folders names to be filtered.')
    args = parser.parse_args()

    def check_urls():
        if args.internal is None:
            parser.error('Internal repository url should be specified as the following: --internal=<url> or -i=<url>')
        if args.external is None:
            parser.error('External repository url should be specified as the following: --external=<url> or -e=<url>')


    if args.publish:
        check_urls()
        if args.branch is None:
            parser.error('branch argument is required when using -p/--publish.')
        Synchronizer().sync_internal_external(
                                            src_repo_url=args.internal, 
                                            dst_repo_url=args.external,
                                            branch_name=args.branch,
                                            filter_map_path=args.filter_map)
    elif args.fetch:
        check_urls()
        if args.prefix is None:
            parser.error('branch prefix argument is required when using -f/--fetch.')

        Synchronizer().sync_external_internal(
                                            internal_repo_url=args.internal, 
                                            external_repo_url=args.external,
                                            prefix=args.prefix
                                            )

    else:
        print(get_logo())
        parser.print_help()




def get_logo():
    logo = '''


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

