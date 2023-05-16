from Synchronizer import Synchronizer
import sys
import utils
import argparse

def main():
	
    parser = argparse.ArgumentParser(
        description =   'Welcome to BunkerSync tool!')
    
    
    parser.add_argument('-p', '--publish', action='store_true', help='Option to publish a given branch from internal repository to external repository.')
    parser.add_argument('-f', '--fetch', action='store_true', help='Option to fetch all new branches with a given prefix from external repository to the internal repository.')
    parser.add_argument('-i', '--internal',action='store',default=None,  type = str, help = 'Internal repository url.')
    parser.add_argument('-e', '--external',action='store', default=None, type = str, help = 'External repository url.')
    parser.add_argument('-b', '--branch', default= None, action='store', type = str, help = '(Required when -p is on) Name of internal branch to be published to external repository.')
    parser.add_argument('-@', '--prefix', default= None, action='store', type = str, help = '(Required when -f is on) Prefix of external branches to be pulled to internal repository.')
    parser.add_argument('-fm', '--filter_map', default= None, action='store', type=str, help = 'Path of the filtering map that includes files or folders names to be filtered.')
    parser.add_argument('-ib', '--internal_branch', default = None, type = str, help = 'The name of the branch in the internal repository.') #todo
    parser.add_argument('-eb', '--external_branch', default = None, type = str, help = 'The name of the branch in the external repository.')#todo
    parser.add_argument('-bb', '--branch_base', default = None, type = str, help = 'The base branch name to be base of new branch.')#todo
    
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
        prefix_fetch = not(args.prefix is None)
        branch_fetch = not((args.internal_branch is None)) or not((args.external_branch is None)) or not((args.branch_base is None))
        
        if prefix_fetch:
            Synchronizer().sync_external_internal_with_prefix(
                                                internal_repo_url=args.internal, 
                                                external_repo_url=args.external,
                                                prefix=args.prefix
                                                )
        elif branch_fetch:            
            if args.internal_branch is None:
                parser.error('internal_branch argument is required when using -f/--fetch.')
            elif args.external_branch is None:
                parser.error('external_branch argument is required when using -f/--fetch.')
            elif args.branch_base is None:
                parser.error('branch_base argument is required when using -f/--fetch.')
            else:
                Synchronizer().sync_external_internal_with_branch(internal_repo_url=args.internal, external_repo_url=args.external, src_branch_base=args.branch_base, )
        else:                   
            parser.error('When using -f/--fetch, one of two following cases is required (1) --prefix \n (2) --internal_branch, --external_branch and --branch_base')



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

