#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=line-too-long,missing-module-docstring,exec-used

import os
import distutils
import setuptools
from setuptools.command.install import install

from lisaconstants.constants import Constant
from lisaconstants.cheader import HeaderGenerator


class PostInstall(install):
    """Handles installation scripts."""
    def run(self):
        install.run(self)
        generator = HeaderGenerator(Constant.ALL)
        install_dir = os.path.join(distutils.sysconfig.get_config_var('prefix'), 'include')
        os.makedirs(install_dir, exist_ok=True)
        generator.write(os.path.join(install_dir, 'lisaconstants.hpp'), 'c++')
        generator.write(os.path.join(install_dir, 'lisaconstants.h'), 'c')


with open('README.md', 'r') as fh:
    long_description = fh.read()

meta = {}
with open('lisaconstants/meta.py') as file:
    exec(file.read(), meta)

setuptools.setup(
    name="lisaconstants",
    version=meta['__version__'],
    author=meta['__author__'],
    author_email=meta['__email__'],
    description="LISA Python Constants provides values sanctioned by the LISA Consortium for physical constants and mission parameters.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.in2p3.fr/lisa-simulation/constants",
    packages=setuptools.find_packages(),
    install_requires=[],
    python_requires='>=3.7',
    cmdclass={'install': PostInstall},
)
