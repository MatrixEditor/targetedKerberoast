#!/usr/bin/env python
import glob
import os

from setuptools import setup

PACKAGE_NAME = "targeted_kerberoast"

VER_MAJOR = 0
VER_MINOR = 1
VER_MAINT = 0
VER_PREREL = "dev"


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name=PACKAGE_NAME,
    version="{}.{}.{}.{}".format(VER_MAJOR, VER_MINOR, VER_MAINT, VER_PREREL),
    description="Targeted Kerberoasting tool: print 'kerberoast' hashes for user accounts that have a SPN set",
    url="https://github.com/ShutdownRepo/targetedKerberoast",
    author="Shutdown (@_nwodtuhs)",
    license="GNU GPLv3",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    platforms=["Unix", "Windows"],
    scripts=[os.path.join(".", "targetedKerberoast.py")],
    install_requires=["impacket", "pyasn1", "rich", "ldap3", "pycryptodome"],
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
    ],
)
