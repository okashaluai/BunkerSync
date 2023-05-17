from setuptools import find_packages, setup

with open("app/Readme.md", "r") as f:
    long_description = f.read()

setup(
    name="BunkerSync",
    version="0.0.20",
    description="""BunkerSync simplifies Git repository syncing. 
                   Sync internal and external repositories with branch filtering and automatic syncing. 
                   Ideal for developers who need to keep repositories in sync.""",
    package_dir={"": "app"},
    packages= find_packages(where="app"),
    long_description= long_description ,
    long_description_content_type = "text/markdown",
    url= "https://github.com/okashaluai/BunkerSync.git",
    author= "Luai Okasha",
    author_email= "LuaiOkasha@gmail.com",
    license="Apache",
    classifiers=[
            "License :: OSI Approved :: Apache Software License",
            "Programming Language :: Python :: 3.11", 
            "Operating System :: OS Independent"
    ],
    install_requires = ["git >= 2.40.0"],
    extra_require={},
    python_requires = ">=3.11"
)
