from setuptools import setup, find_packages

#use for consistent encoding
from codecs import open
from os import path


# local base directory
LOCAL_DIR = path.abspath(path.dirname(__file__))


# Get library description from README.md
with open(path.join(LOCAL_DIR, 'README.md'), encoding='utf-8') as file:
    package_description = file.read()


setup(
    name="int2str",
    packages=find_packages(include=['int2str']),
    version="0.1.0",
    description="Small int to words library",
    long_description=package_description,
    long_description_content_type="text/markdown",
    url="https://int2str.readthedocs.io",
    author="Jarlinton Zea",
    author_email="jarlinton.zeastudio@outlook.com",
    test_suite='tests',
    license="MIT"
)
