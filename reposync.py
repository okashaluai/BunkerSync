from Synchronizer import Synchronizer
import os
import sys
def main(args):
    if (len(args)) is 3:
        source_repo_url = args[0]
        target_repo_url = args[1] 
        branch = args[2]
    else:
        source_repo_url = 'https://github.com/okashaluai/source.git'
        target_repo_url = 'https://github.com/okashaluai/target-repo.git'
        branch = 'b1'

    Synchronizer().run(source_repo_url, target_repo_url, branch)

    input('Press any key to exit.')
    
if __name__ == "__main__":
    main(sys.argv)

 