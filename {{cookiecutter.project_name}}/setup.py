#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
from os.path import exists


if exists("requirements.txt"):
    with open("requirements.txt") as f:
        install_requires = f.read().strip().split("\n")
else:
    install_requires = ["dask", "xarray"]

if exists("README.rst"):
    with open("README.rst") as f:
        long_description = f.read()
else:
    long_description = ""


setup(
    name='{{ cookiecutter.project_name }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=long_description,
    maintainer='{{ cookiecutter.maintainer_full_name }}',
    maintainer_email='{{ cookiecutter.maintainer_email }}',
    url='https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_name }}',
    packages=find_packages(),
    package_dir={'{{ cookiecutter.project_name }}': '{{ cookiecutter.project_name }}'},
    include_package_data=True,
    install_requires=install_requires,
    license='{{ cookiecutter.open_source_license }}',
    zip_safe=False,
    keywords='{{ cookiecutter.project_name }}',
    use_scm_version=True,
    setup_requires=['setuptools_scm', 'setuptools>=30.3.0', 'setuptools_scm_git_archive'],
)