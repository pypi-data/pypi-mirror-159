"""Compile source code and setup Python 3 package"""
import re
from pathlib import Path

from setuptools_scm import get_version
from skbuild import setup as sksetup

__version__ = get_version(root=".", relative_to=__file__)
build_ver = ".".join(__version__.split(".")[:3]).split(".dev")[0]
for i in (Path(__file__).resolve().parent / "_skbuild").rglob("CMakeCache.txt"):
    i.write_text(re.sub("^//.*$\n^[^#].*pip-build-env.*$", "", i.read_text(), flags=re.M))
setup_kwargs = {'use_scm_version': True, 'packages': ["dcm2niix"]}
try:
    sksetup(cmake_languages=("CXX",), cmake_minimum_required_version="3.18", **setup_kwargs)
except:
    from setuptools import setup
    setup(**setup_kwargs)
