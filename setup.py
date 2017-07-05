import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "nycprop-identity",
    version = "0.0.1",
    author = "wstlabs",
    author_email = "wst@pobox.com",
    description = ("validators for bbl and bin"),
    license = "BSD",
    keywords = "pluto acris",
    url = "http://packages.python.org/nycprop-identity",
    packages=['nycprop'],
    long_description=read('README.rst'),
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 2 - Pre-Alpha",
        "Topic :: Utilities",
    ],
)

