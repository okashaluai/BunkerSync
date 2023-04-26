from Synchronizer import Synchronizer

def main():

    source_repo_url = 'https://github.com/okashaluai/Logical-Foundations-Using-Coq.git'
    target_repo_url = None
    branch = None

    Synchronizer().run(source_repo_url, target_repo_url, branch)


if __name__ == "__main__":
    main()
