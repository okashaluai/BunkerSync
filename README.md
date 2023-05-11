# BunkerSync

                                                        *-+-+-+-+-+-+-+-+-+-+-+*
                                                        |         .--.         |
                                                        |        / {} \        |
                                                        |_______/  /\  \_______|
                                                        |#######| |  | |#######|
                                                        |#######`-'++'-´#######|
                                                        *-+-+-+BunkerSync+-+-+-*

BunkerSync is a Python script that simplifies the process of syncing Git repositories. With BunkerSync, you can easily sync an internal repository with an external one and sync new branches from the external repository to the internal repository with support for filtering. BunkerSync is customizable and easy to use, making it an ideal tool for developers who need to keep their repositories in sync.

## Getting Started
## Command-line Arguments
&emsp; **-p**,&emsp;&emsp; &emsp;&ensp; **--publish** &emsp;&emsp; &emsp;&emsp;&nbsp;       Option to publish a given branch from internal repository to external repository.\
&emsp; **-f**,&emsp;&emsp; &emsp;&ensp;&nbsp; **--fetch** &emsp;&emsp; &emsp;&emsp;&emsp;&nbsp;         Option to fetch all new branches with a given prefix from external repository to the internal repository.\
&emsp; **-i**,&emsp;&emsp; &emsp;&ensp;&nbsp; **--internal** &emsp;&emsp; &emsp;&emsp;&nbsp;      Internal repository url.\
&emsp; **-e**,&emsp;&emsp; &emsp;&ensp; **--external** &emsp;&emsp; &emsp;&emsp;      External repository url.\
&emsp; **-b**,&emsp;&emsp; &emsp;&ensp; **--branch** &emsp;&emsp; &emsp;&emsp;&ensp;        (Required when -p is on) Name of internal branch to be published to external repository.\
&emsp; **-@**,&emsp;&emsp; &emsp;&ensp;**--prefix** &emsp;&emsp; &emsp;&emsp;&emsp;        (Required when -f is on) Prefix of external branches to be pulled to internal repository.\
&emsp; **-fm**,&emsp;&emsp; &emsp; **--filter_map** &emsp;&emsp; &emsp;    Path of the filtering map that includes files or folders names to be filtered.

## Contributing

If you have any issues or suggestions for BunkerSync, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/okashaluai/BunkerSync). 

## License

BunkerSync is released under the Apache License. See the [LICENSE](https://github.com/okashaluai/BunkerSync/blob/main/LICENSE) file for details.
