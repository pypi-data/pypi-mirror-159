from setuptools import setup, find_packages

from codecs import open
from os import path

HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ponte',
    version="0.0.1",
    description='A mini-library to process arrays to .json files and viceversa. Developed to pass arrays between Python and C++ through the use of json DOK files.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrewrgarcia/ponte",
    author="Andrew Garcia, PhD",
    license="MIT",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Operating System :: OS Independent"
    ],
    packages=["ponte"],
    include_package_data=True,
    install_requires=["numpy"]
)
