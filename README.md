# BunkerSync

                                                                                                       
                                                                                                       
                                                                                                       
                                      *-+-+-+-+-+-+-+-+-+-+-+*                  +++++++++++++++++            
                                      |         .--.         |                  +               +          
                                      |        / {} \        |                  +    External   +          
                                      |_______/  /\  \_______|----------------+ +   REPOSITORY  +
                                      |#######| |  | |#######|                  +               +
                                      |#######`-'++'-´#######|                  +++++++++++++++++
                                      *-+-+-+BunkerSync+-+-+-*
                                                |
                                                |
                                                |
                                                |
                                                +   
                                         +++++++++++++++++
                                         +               +
                                         +    Internal   +
                                         +   REPOSITORY  +
                                         +               +
                                         +++++++++++++++++

BunkerSync is a Python script that simplifies the process of syncing Git repositories. With BunkerSync, you can easily sync an internal repository with an external one and sync new branches from the external repository to the internal repository with support for filtering. BunkerSync is customizable and easy to use, making it an ideal tool for developers who need to keep their repositories in sync.

## Use cases [TO-UPDATE]
  1. Publish an internal branch into external branch with option to filter.
  2. Fetch external branches whose names startes with given prefix into internal branch.
  3. Fetch a specific external branch into internal branch.

## Prerequisites
  1. Python >= 3.11
  2. installed git

## Getting Started
  1. Use Case 1:
      > BunkerSync -p -i=<internal_repo_url> -e=<external_repo_url> -ib=<internal_name_for_fetched_branch> -eb=<external_branch_to_fetch> -bb=<base_of_internal_fetched_branch> -fm=<path_of_filter_map>
  3. Use Case 2:
      > BunkerSync -f -i=<internal_repo_url> -e=<external_repo_url> -@=<prefix> -bb=<internal_base_of_fetched_branch>  
  4. Use Case 3:
      > BunkerSync -f -i=<internal_repo_url> -e=<external_repo_url> -eb=<external_branch_to_fetch> -ib=<internal_name_for_fetched_branch> -bb=<base_of_internal_fetched_branch>
  * **-bb** is optional, default base would be 'master' branch, could be found in config.py file.
  * **-fm** is optional, otherwise no filtering would be executed.
  * In case you are not sure if you understood the args, see CLI Args below.

## Command-line Arguments
  
  &emsp; **-p**,&emsp;&emsp; &emsp;&ensp; **--publish** &emsp;&emsp; &emsp;&emsp;&nbsp;&emsp;       Option to publish a given branch from internal repository to external repository.\
  &emsp; **-f**,&emsp;&emsp; &emsp;&ensp;&nbsp; **--fetch** &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;         Option to fetch all new branches with a given prefix from external repository to the internal repository.\
  &emsp; **-i**,&emsp;&emsp; &emsp;&ensp;&nbsp; **--internal** &emsp;&emsp; &emsp;&emsp;&nbsp;&emsp;      Internal repository url.\
  &emsp; **-e**,&emsp;&emsp; &emsp;&ensp; **--external** &emsp;&emsp; &emsp;&emsp;&emsp;     External repository url.\
  &emsp; **-@**,&emsp;&emsp; &emsp;&ensp;**--prefix** &emsp;&emsp; &emsp;&emsp;&emsp;&emsp;        (Required when -f is on) Prefix of external branches to be pulled to internal repository.\
  &emsp; **-fm**,&emsp;&emsp; &emsp; **--filter_map** &emsp;&emsp; &emsp;                    Path of the filtering map that includes files or folders names to be filtered.\
  &emsp; **-ib**,&emsp;&emsp; &emsp; **--internal_branch** &emsp;&emsp; &emsp;               (Required when -f is on)The name of the branch in the internal repository.\
  &emsp; **-eb**,&emsp;&emsp; &emsp; **--external_branch** &emsp;&emsp; &emsp;               (Required when -f is on) The name of the branch in the external repository.\
  &emsp; **-bb**,&emsp;&emsp; &emsp; **--branch_base** &emsp;&emsp; &emsp; The base branch name to be the base of the new fetched branch.

## Notes [TO-UPDATE]
  1. Be aware that the tool may ask for authentication credentials with git, the authentication is processed directly against git.
  2. The merge is processed in overwrite manner.
## Contributing

If you have any issues or suggestions for BunkerSync, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/okashaluai/BunkerSync). 

## License

BunkerSync is released under the Apache License. See the [LICENSE](https://github.com/okashaluai/BunkerSync/blob/main/LICENSE) file for details.
