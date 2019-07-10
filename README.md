# Purpose

Modified from [https://github.com/crwilcox/my-pypi-package](crwilcox/my-pypi-package) to be a starter project suitable for how I tend to code, rather than a starting point for creating a package intended for upload to PyPi as in crwilcox's repository.

## Modifications:

- Use `venv` instead of `virtualenv` to create virtual environment.
- Add `black` and `pylint` to required packages in `setup.py`.
- Use `pip install -e .` after virtual environment is set up so that local package being developed is in develop mode and can be dynamically changed without having to re-install. This command also installs all required packages spectified in `setup.py` (rather than using a `requirements.txt` file).
- Add `.vscode/settings.json` and set to (1) use `black` on file save and (2) use the local virtual environment.
- Add `.gitignore` with appropriate settings, including ignoring the local virtual envronment files in `./env/`.
- Delete `noxfile.py` since I don't use this.

## Organization

    ├── README.md
    ├── code_and_notebooks_to_use_package_during_development
    │   └── purpose_of_this_directory.md
    ├── mypackage
    │   ├── __init__.py
    │   └── mypackage.py
    ├── setup.py
    └── tests
        └── test_mypackage.py

## Information

Another good resource is [Chris Wilcox - Shipping your first Python package and automating future publishing - PyCon 2019](https://www.youtube.com/watch?v=P3dY3uDmnkU).

# Quick Start

## Supported Python Versions

Python >= 3.5

## Mac

I have Anaconda python installed on my laptop. My base conda environment uses Python 3.6. I have also have a conda environment, `py37`, that has Python 3.7 installed. To use Python 3.7 in the virtual environment created with this project, I would do the following.

    # Get starter project and name it `myproject`
    $ git clone https://github.com/gregnordin/starter_project_files.git myproject

    # `cd` into directory and re-initialize git so I can start fresh
    $ cd myproject
    $ rm -rf .git
    $ git init

    # Activate conda environment `p37` where Python 3.7 is installed. Doing so means that when I use `venv` to create
    # a local virtual environment, it will pull from Python 3.7 and therefore be a Python 3.7 local virtual environment.
    $ source activate py37
    (py37)
    $ python -m venv env   # `env` is the name I have chosen for my virtual environment and its corresponding directory

    # Deactivate the conda environment, otherwise using `pip install` will install packages into it instead of `env`
    $ conda deactivate

    # Activate new virtual environment
    $ source env/bin/activate

    # Install packages specified in setup.py
    (env)
    $ pip install -e .

    # Install any other desired packages using the following pattern
    (env)
    $ pip install <some_package>

    # Now I am all set to work in the new virtual environment

    # To get out of the virtual environment when I am done working in it do the the following
    (env)
    $ deactivate

If instead of using Python 3.7 in `env` I wanted to use Python 3.6, I would do the same as above except eliminate the commands `source activate py37` and `conda deactivate`. Likewise, if I had some other python version in another conda environment, say <conda_env>, on which I would like to base my local virtual environment, I would activate that conda environment in place of `py37` above, i.e., `source activate <conda_env>` and then create the virtual environment, `env`.

## Windows - ??

To do: figure out and add commands

# Example Usage

```
import mypackage
mypackage.MyPackage().spam()
```
