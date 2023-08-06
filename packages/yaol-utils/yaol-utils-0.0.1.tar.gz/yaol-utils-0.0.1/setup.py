from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Some helpful utility functions'
LONG_DESCRIPTION = 'A package that provides several utility functions and code snippets to simplify the life of a developer.'

# Setting up
setup(
    name="yaol-utils",
    version=VERSION,
    author="Phillip Yao-Lakaschus",
    author_email="<Philliplakaschus@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['varname'],
    keywords=['python', 'util', 'utils', 'print'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)