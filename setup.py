#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#
# To generate DEB package from Python Package:
# sudo pip3 install stdeb
# python3 setup.py --verbose --command-packages=stdeb.command bdist_deb
#
#
# To generate RPM package from Python Package:
# sudo apt-get install rpm
# python3 setup.py bdist_rpm --verbose --fix-python --binary-only
#
#
# To generate EXE MS Windows from Python Package (from MS Windows only):
# python3 setup.py bdist_wininst --verbose
#
#
# To generate PKGBUILD ArchLinux from Python Package (from PyPI only):
# sudo pip3 install git+https://github.com/bluepeppers/pip2arch.git
# pip2arch.py PackageNameHere
#
#
# To Upload to PyPI by executing:
# sudo pip install --upgrade pip setuptools wheel virtualenv
# python3 setup.py bdist_egg bdist_wheel --universal sdist --formats=zip upload --sign


"""Setup.py for Python, as Generic as possible."""


import os
import re
import sys

from setuptools import setup, Command

from zipapp import create_archive


##############################################################################
# EDIT HERE


MODULE_PATH = os.path.join(os.path.dirname(__file__), "microraptor.py")
DESCRIPTION = """Microraptor builds cool presentations using Angler, Impress
and Markdown. Presentations using a simple MarkDown file.
Convert a GitHub README.md to Presentations with one command.
Dont touch a single line of JavaScript code."""


##############################################################################
# Dont touch below


try:
    with open(str(MODULE_PATH), "r", encoding="utf-8-sig") as source_code_file:
        SOURCE = source_code_file.read()
except:
    with open(str(MODULE_PATH),  "r") as source_code_file:
        SOURCE = source_code_file.read()


def find_this(search, source=SOURCE):
    """Take a string and a filename path string and return the found value."""
    print("Searching for {what}.".format(what=search))
    if not search or not source:
        print("Not found on source: {what}.".format(what=search))
        return ""
    return str(re.compile(r".*__{what}__ = '(.*?)'".format(
        what=search), re.S).match(source).group(1)).strip().replace("'", "")


class ZipApp(Command):
    description, user_options = "Creates a zipapp.", []

    def initialize_options(self): pass  # Dont needed, but required.

    def finalize_options(self): pass  # Dont needed, but required.

    def run(self):
        return create_archive("microraptor.py", "microraptor.pyz",
                              "/usr/bin/env python3")


print("Starting build of setuptools.setup().")


##############################################################################
# EDIT HERE


setup(

    name="microraptor",
    version=find_this("version"),

    description="Presentation builder using Markdown and ImpressJS.",
    long_description=DESCRIPTION,

    url=find_this("url"),
    license=find_this("license"),

    author=find_this("author"),
    author_email=find_this("email"),
    maintainer=find_this("author"),
    maintainer_email=find_this("email"),

    include_package_data=True,
    zip_safe=True,

    install_requires=['anglerfish', 'mistune', 'pygments'],
    setup_requires=['anglerfish', 'mistune', 'pygments'],
    tests_require=['anglerfish', 'mistune', 'pygments'],
    requires=['anglerfish', 'mistune', 'pygments'],

    scripts=["microraptor.py"],

    cmdclass={"zipapp": ZipApp},

    keywords=['ImpressJS', 'presentation', 'HTML5', 'Markdown', 'impress',
              'CSS', 'HTML', 'Web', 'GFM', 'KISS', 'Builder', 'HTML'],

    classifiers=[

        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Other Audience',

        'Natural Language :: English',

        'License :: OSI Approved :: GNU General Public License (GPL)',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        'Operating System :: OS Independent',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',

        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',

        'Topic :: Software Development',

    ],
)


print("Finished build of setuptools.setup().")
