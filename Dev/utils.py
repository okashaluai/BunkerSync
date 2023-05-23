import os
import shutil
import subprocess
import urllib.request  
import re
from distutils import dir_util
import stat
import tempfile
import random

def onerror(func, path, exc_info):
    """
    Error handler for ``shutil.rmtree``.

    If the error is due to an access error (read only file)
    it attempts to add write permission and then retries.

    If the error is for another reason it re-raises the error.

    Usage : ``shutil.rmtree(path, onerror=onerror)``
    """
    # Is the error an access error?
    if not os.access(path, os.W_OK):
        os.chmod(path, stat.S_IWUSR)
        func(path)
    else:
        raise

def rm_dir(path):
    """
    Recursively removes a directory and all its contents.

    Args:
        path (str): The path of the directory to be removed.

    Raises:
        Exception: If an error occurs during removal and the `ignore_errors` parameter is set to `False`.

    """
    if os.path.exists(path):
        shutil.rmtree(path, ignore_errors=False, onerror=onerror )
    pass

# def branch_browse(url):
#     webUrl = urllib.request.urlopen(url)  


def check_branch_exists(remote_repo_url, branch_name):
    """This function checks if a branch exists in a remote Git repository given its URL and branch name.

    Args:
        remote_repo_url (Path): The URL of the remote Git repository as a string.
        branch_name (str): The name of the branch as a string.

    Returns:
        _type_: _description_
    """

    try:
        # Run the git ls-remote command to get the list of remote branches
        output = subprocess.check_output(['git', 'ls-remote', '--heads', remote_repo_url], universal_newlines=True)

        # Iterate over the output lines and check if the branch exists
        for line in output.splitlines():
            _, ref = line.split('\t')
            if ref.endswith(branch_name):
                return True

        # If the branch was not found
        return False
    except subprocess.CalledProcessError:
        # Handle any errors that occurred during the git command execution
        print("Failed to run git command.")
        return False

# def find_last_slash(str):
#     """_summary_

#     Args:
#         str (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     res = -1
#     for i in range(len(str)):
#         if str[i] == '/':
#             res = i
#     return res

# def parse_branch_name(full_ref):
#     """_summary_

#     Args:
#         full_ref (_type_): _description_

#     Returns:
#         _type_: _description_
#     """
#     index = find_last_slash(full_ref)
#     branch_name = ""
#     if index > -1:
#         branch_name = full_ref[index + 1:]
#     return branch_name


def copy_dir(from_dir, to_dir):
    """Copy a directory from a source path to a destination path.

    Args:
        from_dir (str): The path of the source directory.
        to_dir (str): The path of the destination directory.
    """
    shutil.copytree(src=from_dir, dst=to_dir, dirs_exist_ok=True)
    pass


def move_dir(src_dir, dst_dir):
    """Move the contents of the `src_dir` to the `dst_dir`.

    If the `dst_dir` already exists, its contents will be replaced with the contents of `src_dir`.

    Args:
        src_dir (str): The source directory to move.
        dst_dir (str): The destination directory to move the source directory to.
    """
    shutil.copytree(src_dir, dst_dir)
    if os.path.exists(src_dir):
        shutil.rmtree(src_dir, ignore_errors=False, onerror=onerror )
    pass


def push_to_remote(local_repo_path):
    """Pushes changes from a local Git repository to its remote counterpart.

    Args:
        local_repo_path (str): The path to the local Git repository.

    Raises:
        CalledProcessError: If a Git command fails.

    """
    subprocess.run(['git', '-C',local_repo_path, 'add', '.'], shell=False)
    subprocess.run(['git', '-C', local_repo_path, 'commit', '-m', 'A branch merged to this branch successfully!' ], shell=False)
    subprocess.run(['git', '-C',local_repo_path, 'push' , 'origin'], shell=False)
    pass

def get_temp_path():
    tmp_dir = tempfile.gettempdir()
    return tmp_dir
    pass

def generate_random_number():
    random.seed(1)
    res = random.random() * (10 ** 12)
    return int(res)

