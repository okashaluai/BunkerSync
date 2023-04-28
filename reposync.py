from Synchronizer import Synchronizer
import os
import sys
def main(args):
    if (len(args)) == 3:
        src_repo_url = args[0]
        dst_repo_url = args[1] 
        branch = args[2]
    else:
        src_repo_url = 'https://github.com/okashaluai/source.git'
        dst_repo_url = 'https://github.com/okashaluai/target-repo.git'
        branch = 'b1'
    
    Synchronizer().run(src_repo_url, dst_repo_url, branch)

    input('Press any key to exit.')
    
if __name__ == "__main__":
    main(sys.argv)

 