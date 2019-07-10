# Purpose

Modified from [https://github.com/crwilcox/my-pypi-package](crwilcox/my-pypi-package) to be a starter project suitable for how I tend to code, rather than a starting point for creating a package intended for upload to PyPi as in crwilcox's repository.

## Modifications:

- Use `venv` instead of `virtualenv` to create virtual environment
- Add `black` and `pylint` to required packages in `setup.py`
- Use `pip install -e .` after virtual environment is set up so that local package being developed is in develop mode and can be dynamically changed without having to re-install. This command also installs all required packages spectified in `setup.py` (rather than using a `requirements.txt` file).
- Add `.vscode/settings.json` and set to use `black` on file save and the local virtual environment
- Add `.gitignore` with appropriate settings, including ignoring the local virtual envronment files in `./env/`
- Delete `noxfile.py` since I don't use this

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

## Mac/Linux

```
python -m venv <your-env>
source <your-env>/bin/activate
pip install -e .            # Note: this will install all packages specified in setup.py in the activated virtual environment
pip install <some_package>  # Install additional packages
```

## Windows - ??

```
#python -m venv <your-env>
#<your-env>\Scripts\activate
#<your-env>\Scripts\pip.exe install google-cloud-firestore
#pip install <some_package> (?)
```

# Example Usage

```
import mypackage
mypackage.MyPackage().spam()
```
