from Synchronizer import Synchronizer
import sys
import utils

def main(args):
    logo = '''
    .-.   .-.  .--.  .--. .--. .-..-. .--.  
    |  `.'  | / {} \ | {} |/ {} \| ||  `| |   
    | |\ /| |/  /\  \|  __|\  /\  /| || |\ |  
    | | V | || |  | || |__ | |  | || || | \ \ 
    |_|   |_|`-'  `-'`-'  `-'  `-'`-'`-'  `-'

    '''

    print(logo)

           
    if (len(args)) == 3:
        src_repo_url = args[0]
        dst_repo_url = args[1] 
        branch = args[2]
    else:
        src_repo_url = 'https://github.com/okashaluai/internal.git'
        dst_repo_url = 'https://github.com/okashaluai/external.git'
        branch = 'b1'
    
    # Synchronizer().sync_internal_external(src_repo_url, dst_repo_url, branch)
    # Synchronizer().sync_external_internal(src_repo_url, dst_repo_url)

    # utils.move_dir('./temp/.git', './dst')
    input('Press any key to exit.')
     
if __name__ == "__main__":
    main(sys.argv)

