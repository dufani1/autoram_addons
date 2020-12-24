# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in autoram_addons/__init__.py
from autoram_addons import __version__ as version

setup(
	name='autoram_addons',
	version=version,
	description='addons and customizations for autoram',
	author='Ebkar Technology.',
	author_email='admin@ebkar.ly',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
