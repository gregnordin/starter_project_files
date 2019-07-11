import setuptools

with open("README.md") as f:
    long_description = f.read()

setuptools.setup(
    name="mypackage",
    version="0.0.1",
    description="My first package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=setuptools.find_packages(),
    url="https://github.com/gregnordin/starter_project_files",
    author="Greg Nordin",
    author_email="nordin@byu.edu",
    classifiers=[
        "Development Status :: 1 - Alpha",
        "License :: OSI Approved :: MIT",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ],
    install_requires=["black", "pylint"],
)
