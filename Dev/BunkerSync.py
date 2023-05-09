from Synchronizer import Synchronizer
import sys
import utils
import argparse

def main(args):
    
    if (len(args)) == 3:
        src_repo_url = args[0]
        dst_repo_url = args[1] 
        branch = args[2]
    else:
        src_repo_url = 'https://github.com/okashaluai/internal.git'
        dst_repo_url = 'https://github.com/okashaluai/external.git'
        branch = 'b1'
    
    # Synchronizer().sync_internal_external(src_repo_url, dst_repo_url, branch)
    #Synchronizer().sync_external_internal(src_repo_url, dst_repo_url)
	
    print(get_logo())
    parser = argparse.ArgumentParser(
        description =   'Welcome to BunkerSync tool!')
    
    
    parser.add_argument('-p', '--publish', action='store_true')
    parser.add_argument('-f', '--fetch', action='store_true')
    parser.add_argument('-i', '--internal', metavar='internal', action='store', type = str, help = 'Internal repository url.')
    parser.add_argument('-e','--external',metavar='external', action='store', type = str, help = 'External repository url.')
    parser.add_argument('-b', '--branch', action='store', type = str, help = 'Name of internal branch to be published to external repository.')

    case = parser.parse_intermixed_args(['--publish', '--fetch'])
    
    if case.publish:
        
        args = parser.parse_intermixed_args(['internal', 'external'])

        Synchronizer().sync_internal_external(
                                                src_repo_url=args.internal, 
                                                dst_repo_url=args.external,
                                                branch_name=args.branch)
        pass

        # if args.fetch:
        #     pass
        


    # parser.add_argument('-fm', '--filter_map', metavar = 'filter_map_path', type=str, help = 'Path of the filtering map that includes files or folders names to be filtered.')
    # parser.add_argument('-@', '--prefix', metavar = 'prefix', type = str, help = 'Prefix of external branches to be pulled to internal repository.')
    # parser.add_argument('branch', type = str, help = 'Name of internal branch to get published to external repository.')

    # parser.add_argument('internal', type = str, help = 'Internal repository url.')
    # parser.add_argument('external', type = str, help = 'External repository url.')
    # args = parser.parse_args()

    # if args.publish:
    #     parser.add_argument('branch', type = str, help = 'Name of internal branch to get published to external repository.')
    #     args = parser.parse_args()
    #     Synchronizer().sync_internal_external(src_repo_url=args.internal, dst_repo_url=args.external, branch_name=args.branch)

    #     pass

    # if args.fetch:
    #     pass

    # if args.fetch and args.publish:
    #     Synchronizer().sync_external_internal(external_repo_url=args.external_repo_url, internal_repo_url=args.internal_repo_url)
    #     # Synchronizer().sync_internal_external(external_repo_url=args.external_repo_url, internal_repo_url=args.internal_repo_url, branch_name=)
    # elif args.fetch:
    #     Synchronizer().sync_external_internal(external_repo_url=args.external_repo_url, internal_repo_url=args.internal_repo_url)
    # elif args.publish:
    #     pass
    #     # Synchronizer().sync_internal_external(external_repo_url=args.external_repo_url, internal_repo_url=args.internal_repo_url, branch_name=)
    # else:
    #     parser.argument_default('-h')



def get_logo():
    logo = '''
     *-+-+-+-+-+-+-+-+-+-+-+*
     |         .--.         |
     |        / {} \        |
     |_______/  /\  \_______|
     |#######| |  | |#######|
     |#######`-'++'-´#######|
     *-+-+-+BunkerSync+-+-+-*
    
    
    '''
	
    return logo



if __name__ == "__main__":
    main(sys.argv)

