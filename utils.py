import os
import shutil
import subprocess
import urllib.request  
import re

def rm_dir(path):
    def onerror(func, path, exc_info):
        """
        Error handler for ``shutil.rmtree``.

        If the error is due to an access error (read only file)
        it attempts to add write permission and then retries.

        If the error is for another reason it re-raises the error.

        Usage : ``shutil.rmtree(path, onerror=onerror)``
        """
        import stat
        # Is the error an access error?
        if not os.access(path, os.W_OK):
            os.chmod(path, stat.S_IWUSR)
            func(path)
        else:
            raise

    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=False, onerror=onerror )
    pass

def branch_browse(url):
    webUrl = urllib.request.urlopen(url)  


def branch_exists(remote_repo_url, branch_name):
    branches  = subprocess.check_output(['git', 'ls-remote' , remote_repo_url,  branch_name ], shell=True)
    wc_l = len(re.findall('refs/heads/'+branch_name+'$', branches.decode('utf-8')))
    if wc_l:
        return True
    else: return False
