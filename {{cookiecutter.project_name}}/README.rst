===============================
{{ cookiecutter.project_name }}
===============================

.. image:: https://img.shields.io/circleci/project/github/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_name }}/master.svg?style=for-the-badge&logo=circleci
    :target: https://circleci.com/gh/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_name }}/tree/master

.. image:: https://img.shields.io/codecov/c/github/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_name }}.svg?style=for-the-badge
    :target: https://codecov.io/gh/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.project_name }}


.. image:: https://img.shields.io/readthedocs/{{ cookiecutter.project_name }}/latest.svg?style=for-the-badge
    :target: https://{{ cookiecutter.project_name }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_name }}.svg?style=for-the-badge
    :target: https://pypi.org/project/{{ cookiecutter.project_name }}
    :alt: Python Package Index
    
.. image:: https://img.shields.io/conda/vn/conda-forge/{{ cookiecutter.project_name }}.svg?style=for-the-badge
    :target: https://anaconda.org/conda-forge/{{ cookiecutter.project_name }}
    :alt: Conda Version


{{ cookiecutter.project_short_description}}.
See documentation_ for more information.

.. _documentation: https://{{ cookiecutter.project_name }}.readthedocs.io


Installation
------------

{{ cookiecutter.project_name }} can be installed from PyPI with pip:

.. code-block:: bash

    pip install {{ cookiecutter.project_name }}


It is also available from `conda-forge` for conda installations:

.. code-block:: bash

    conda install -c conda-forge {{ cookiecutter.project_name }}