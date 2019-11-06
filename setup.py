# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in qct_energy/__init__.py
from qct_energy import __version__ as version

setup(
	name='qct_energy',
	version=version,
	description='qct energy',
	author='suraj varade',
	author_email='varade.suraj787@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
