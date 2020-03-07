# Purpose

Starter project suitable for how I tend to develop project code.

## Features:

- Use built in `venv` to create virtual environment.
- Add `black` and `pylint` to required packages in `setup.py`.
- Add my usually needed packages (`numpy`, `matplotlib`, `jupyterlab`, `ipykernel`) to `setup.py`
- Use `pip install -e .` after virtual environment is set up so that local package being developed is in develop mode and can be dynamically changed without having to re-install. This command also installs all required packages spectified in `setup.py` (rather than using a `requirements.txt` file).
- Add `.vscode/settings.json` and set to (1) use `black` on file save and (2) use the local virtual environment.
- Add `.gitignore` with appropriate settings, including ignoring the local virtual envronment files in `env/`.

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

### Install

I have Anaconda python installed on my laptop. My base conda environment uses Python 3.6. I have also have a conda environment, `py37`, that has Python 3.7 installed. To use Python 3.7 in the virtual environment created with this project, I would do the following.

    # 1. Get starter project and name it <newproject>
    $ git clone https://github.com/gregnordin/starter_project_files.git <newproject>

    # 2. `cd` into directory and re-initialize git so I can start fresh
    $ cd <newproject>
    $ rm -rf .git
    $ git init

    # 3. Rename directory `myproject` to `<newproject>` so that I have the desired package name
    $ mv myproject/ <newproject>/

    # 4. Manually edit `startup.py`, minimally changing name and description in setuptools.setup

    # 5. Manually edit `README.md` to reflect the purpose of <newproject>

    # 6. Activate conda environment `p37` where Python 3.7 is installed. Doing so means that when I use `venv` to create
    # a local virtual environment, it will pull from Python 3.7 and therefore be a Python 3.7 local virtual environment.
    $ source activate py37
    (py37)
    $ python -m venv .venv --prompt <text for prompt>
    # `.venv` is the my virtual environment and <text for prompt> will appear above my cursor when I activate it

    # 7. Deactivate the conda environment, otherwise using `pip install` will install packages into it instead of `env`
    $ conda deactivate

    # 8. Activate new virtual environment
    $ source env/bin/activate

    # 9. Install packages specified in setup.py
    (env)
    $ pip install -e .

    # 10. Install any other desired packages using the following pattern
    (env)
    $ pip install <some_package>

    # 11. Now I am all set to work in the new virtual environment

    # 12. To get out of the virtual environment when I am done working in it do the the following
    (env)
    $ deactivate

If instead of using Python 3.7 in `env` I wanted to use Python 3.6, I would do the same as above except eliminate the commands `source activate py37` and `conda deactivate`. Likewise, if I had some other python version in another conda environment, say <conda_env>, on which I would like to base my local virtual environment, I would activate that conda environment in place of `py37` above, i.e., `source activate <conda_env>` and then create the virtual environment, `env`.

### Re-build virtual environment

Sometimes during development I want to re-build my virtual environment. These are the steps I follow.

    # Make sure the virtual environment is deactivated
    $ deactivate

    # Delete virtual environment
    $ rm -rf env

    # Delete egg-info
    $ rm -rf  *.egg-info

    # Start at Step 6 above and re-install virtual environment

### How to use Jupyter Lab (similar for Jupyter Notebooks)

#### Set up environment to use it as a jupyter kernel

    # with virtual environment activated:
    (env)
    $ python -m ipykernel install --user --name=<newpackage>

    # Before executing this command:
    (env)
    $ jupyter kernelspec list
    Available kernels:
    3d_print_job_preparation    /Users/nordin/Library/Jupyter/kernels/3d_print_job_preparation
    javascript                  /Users/nordin/Library/Jupyter/kernels/javascript
    python3                     /Users/nordin/Library/Jupyter/kernels/python3
    python2                     /usr/local/share/jupyter/kernels/python2

    # After executing this command:
    (env)
    $ jupyter kernelspec list
    Available kernels:
    3d_print_job_preparation    /Users/nordin/Library/Jupyter/kernels/3d_print_job_preparation
    javascript                  /Users/nordin/Library/Jupyter/kernels/javascript
    <newpackage>                /Users/nordin/Library/Jupyter/kernels/mypackage
    python3                     /Users/nordin/Library/Jupyter/kernels/python3
    python2                     /usr/local/share/jupyter/kernels/python2

#### Start jupyterlab (regular)

    # Start jupyterlab
    (env)
    $ jupyter lab

#### Start jupyterlab (background)

    # Start jupyterlab in the background so the terminal remains free to use
    (env)
    $ nohup jupyter lab &

    # Kill jupyterlab that's running in the background
    $ jupyter notebook list
        Currently running servers:
        http://localhost:8888/?token=blah :: /Users/nordin/Documents/Projects/Python/190709_starter_project_files
    # Note the port jupyter is running on (8888). Use this to find the PID of the jupyter process
    $ lsof -n -i4TCP:8888
        COMMAND     PID   USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
        python3.7 38870 nordin    8u  IPv4 0xb27f89b37e23f69b      0t0  TCP 127.0.0.1:ddi-tcp-1 (LISTEN)
    # Now kill the jupyter process
    $ kill 38870

### Remove jupyter kernel

    $ jupyter kernelspec uninstall <kernel_to_uninstall>

### Use TOC with jupyterlab

    (env)
    $ jupyter labextension install @jupyterlab/toc

### Use jupyter_contrib_nbextensions with jupyter notebooks

    Only works with `jupyter notebook`, not 'jupyter lab`

    (env)
    $ pip install jupyter_contrib_nbextensions
    (env)
    $ jupyter contrib nbextension install --sys-prefix

In the last command, `--sys-prefix` is the critical part to get the extensions installed locally in the virtual environment.

## Windows - ??

To do: figure out and add commands

# Example Usage

```
import <newpackage>
<newpackage>.MyPackage().spam()
```
