# Purpose

Starter project suitable for how I tend to develop project code.

## Features:

- Use built in `venv` to create virtual environment in `.venv` directory.
- Add `black` and `pylint` to required packages in `setup.py` (see [How to create a setup file for your project](https://www.pythonforthelab.com/blog/how-create-setup-file-your-project/) for a good explanation of the how and why of using `setup.py`).
- Add my usually needed packages (`numpy`, `matplotlib`, `jupyterlab`, `ipykernel`) to `setup.py`
- Use `pip install -e .` after virtual environment is set up so that local package being developed is in develop mode and can be dynamically changed without having to re-install. This command also installs all required packages spectified in `setup.py` (rather than using a `requirements.txt` file).
- Add `.vscode/settings.json` and set to (1) use `black` on file save and (2) use the local virtual environment.
- Add `.gitignore` with appropriate settings, including ignoring the local virtual envronment files in `.venv/`.

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

A good resource is [Chris Wilcox - Shipping your first Python package and automating future publishing - PyCon 2019](https://www.youtube.com/watch?v=P3dY3uDmnkU). See also [Ultimate Setup for Your Next Python Project](https://towardsdatascience.com/ultimate-setup-for-your-next-python-project-179bda8a7c2c), [Python Application Layouts: A Reference](https://realpython.com/python-application-layouts/), [How to Set Up a Python Project For Automation and Collaboration](https://eugeneyan.com/writing/setting-up-python-project-for-automation-and-collaboration/). 11/7/20 - Alternatively, use new `setup.cfg` approach, for example see Problem 2 at [Packaging in Python: Tools and Formats](https://towardsdatascience.com/packaging-in-python-tools-and-formats-743ead5f39ee). 1/1/22 - Alternatively, follow [Set up your project](https://goodresearch.dev/setup.html) in [The Good Research Code Handbook](https://goodresearch.dev/index.html) and use the associated CookieCutter template. Makes good case for use of `pip install -e` with the virtual environment over modifying the python `PATH`.

# Quick Start

## Supported Python Versions

Python >= 3.5

## Mac

### Install

I have set up python on my macbook pro according to https://github.com/gregnordin/python_setup_macbook. For the following I want the virtual environment to be based on a conda environment, `py37`, that has Python 3.7 installed.

    # 1. Get starter project and name it <newproject>
    $ git clone https://github.com/gregnordin/starter_project_files.git <newproject>

    # 2. `cd` into directory and re-initialize git so I can start fresh
    $ cd <newproject>
    $ rm -rf .git
    $ git init

    # 3. Rename directory `myproject` to `<newproject>` so that I have the desired package name
    $ mv myproject/ <newproject>/

    # 4. Manually edit `startup.py`. At a minimum, name and description should be changed in setuptools.setup.

    # 5. Manually edit `README.md` to reflect the purpose of <newproject>.

    # 6. Activate conda environment `p37` where Python 3.7 is installed. Doing so means that when I use `venv` to create
    # a local virtual environment, it will pull from Python 3.7 and therefore be a Python 3.7 local virtual environment.
    $ source activate py37
    (py37)
    $ python -m venv .venv --prompt <text for prompt>
    # `.venv` is the my virtual environment directory and <text for prompt> will appear above each command line after the virtual environment is activated

    # 7. Deactivate the conda environment, otherwise using `pip install` will install packages into it instead of `.venv`
    $ conda deactivate

    # 8. Activate new virtual environment
    $ source .venv/bin/activate

    # 9. Install packages specified in setup.py
    (<text for prompt>)
    $ pip install -e .

    # 10. Install any other desired packages using the following pattern
    (<text for prompt>)
    $ pip install <some_package>

    # 11. Now I am all set to work in the new virtual environment

    # 12. To get out of the virtual environment when I am done working in it do the the following
    (<text for prompt>)
    $ deactivate

If instead of using Python 3.7 in `.venv` I wanted to use some other python version in another conda environment, say <conda_env>, on which I would like to base my local virtual environment, I would activate that conda environment in place of `py37` above, i.e., `source activate <conda_env>` and then create the virtual environment.

### Re-build virtual environment

Sometimes during development I want to re-build my virtual environment. These are the steps I follow.

    # Make sure the virtual environment is deactivated
    $ deactivate

    # Delete virtual environment
    $ rm -rf .venv

    # Delete egg-info
    $ rm -rf  *.egg-info

    # Start at Step 6 above and re-install virtual environment

### How to use Jupyter Lab (similar for Jupyter Notebooks)

See https://github.com/gregnordin/python_setup_macbook.

## Windows - ??

To do: figure out and add commands

# Example Usage

```
import <newpackage>
<newpackage>.MyPackage().spam()
```
