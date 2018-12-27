#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages
import versioneer
from os.path import exists

readme = open("README.rst").read() if exists("README.rst") else ""



setup(
    name='{{ cookiecutter.project_name }}',
    description='{{ cookiecutter.project_short_description }}',
    long_description=readme,
    maintainer='{{ cookiecutter.full_name }}',
    maintainer_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_name }}',
    packages=[
        '{{ cookiecutter.project_name }}',
    ],
    package_dir={'{{ cookiecutter.project_name }}': '{{ cookiecutter.project_name }}'},
    include_package_data=True,
    install_requires=[
    ],
    license='{{ cookiecutter.open_source_license }}',
    zip_safe=False,
    keywords='{{ cookiecutter.project_name }}',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
)