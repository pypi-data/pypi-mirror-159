from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding='utf-8') as fh:
    long_description = '\n' + fh.read()

VERSION = '0.2.2'
DESCRIPTION = 'Helps shorten the amount of code you write'
LONG_DESCRIPTION = 'A package that shortens the amount of code you have to write for your program with the help of functions.'

# Setting up
setup(
    name="ShrtCde",
    version=VERSION,
    author="Uralstech (Udayshankar Ravikumar)",
    author_email="<info@uralstech.in>",
    url="https://github.com/Uralstech/ShrtCde",
    license="Apache License 2.0",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'code', 'short', 'short code', 'ui', 'sort', 'file', 'io', 'library'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)