import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="mypackage",
    version="0.0.1",
    description="My first package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    author="Greg Nordin",
    author_email="nordin@byu.edu",
    install_requires=[
        "black", 
        "pylint", 
        "numpy", 
        "matplotlib", 
        "jupyterlab", 
        "ipykernel",
    ],
)
