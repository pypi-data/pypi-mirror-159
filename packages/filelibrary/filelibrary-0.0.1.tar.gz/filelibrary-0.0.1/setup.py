import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup_info = {
    "name": "filelibrary",
    "version": "0.0.1",
    "author": "CantCode",
    "author_email": "cantcode023@gmail.com",
    "description": "filelibrary is a simple package that allows you to get and edit files or directories in a specified path.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/CantCode023/filesystem",
    "packages": setuptools.find_packages(),
    "classifiers": [
        "Programming Language :: Python :: 3",
    ],
    "python_requires": '>=3.7'
}


setuptools.setup(**setup_info)