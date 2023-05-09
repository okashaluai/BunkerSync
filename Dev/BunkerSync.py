from Synchronizer import Synchronizer
import sys
import utils
import argparse

def main(args):

    src_repo_url = 'https://github.com/okashaluai/internal.git'
    dst_repo_url = 'https://github.com/okashaluai/external.git'
    branch = 'b1'

	
    print(get_logo())
    parser = argparse.ArgumentParser(
        description =   'Welcome to BunkerSync tool!')
    
    
    parser.add_argument('-p', '--publish', action='store_true')
    parser.add_argument('-f', '--fetch', action='store_true')
    parser.add_argument('internal',action='store', type = str, help = 'Internal repository url.')
    parser.add_argument('external',action='store', type = str, help = 'External repository url.')
    parser.add_argument('-b', '--branch', metavar='branch',default= None, action='store', type = str, help = '(Required when -p is on) Name of internal branch to be published to external repository.')
    parser.add_argument('-@', '--prefix', metavar = 'prefix',default= None, action='store', type = str, help = '(Required when -f is on) Prefix of external branches to be pulled to internal repository.')
    parser.add_argument('-fm', '--filter_map', metavar = 'filter_map_path',default= None, action='store', type=str, help = '(Required when -p is on) Path of the filtering map that includes files or folders names to be filtered.')
    
    args = parser.parse_args()
    
    if args.publish:

        if args.branch is None:
            parser.error('branch argument is required when using -p/--publish.')
        if args.filter_map is None:
            parser.error('filter_map=<path> argument is required when using -p/--publish.')

        # Synchronizer().sync_internal_external(
                                            # src_repo_url=args.internal, 
                                            # dst_repo_url=args.external,
                                            # branch_name=args.branch
                                            # filter_map_path=args.filter_map)
        Synchronizer().sync_internal_external(src_repo_url, dst_repo_url, args.branch)
    elif args.fetch:
        if args.prefix is None:
            parser.error('branch prefix argument is required when using -f/--fetch.')

        #pass prefix
        Synchronizer().sync_external_internal(
                                            internal_repo_url=args.internal, 
                                            external_repo_url=args.external)

    else:
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
                
                author: https://github.com/okashaluai/BunkerSync.git
                Email: Luaiokasha@gmail.com
    
    '''
	
    return logo



if __name__ == "__main__":
    main(sys.argv)

