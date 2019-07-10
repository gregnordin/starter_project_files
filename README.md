Modified from [https://github.com/crwilcox/my-pypi-package](crwilcox/my-pypi-package).

`mypackage` is a sample package made to demonstrate how to create a package of your own

# Quick Start

## Supported Python Versions

Python >= 3.5

## Mac/Linux

```
python -m venv <your-env>
source <your-env>/bin/activate
#<your-env>/bin/pip install google-cloud-firestore
pip install <some_package>
```

## Windows

```
python -m venv <your-env>
<your-env>\Scripts\activate
#<your-env>\Scripts\pip.exe install google-cloud-firestore
pip install <some_package> (?)
```

# Example Usage

```
import mypackage
mypackage.MyPackage().spam()
```