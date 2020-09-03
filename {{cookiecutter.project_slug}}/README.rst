.. image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/CI?logo=github&style=for-the-badge
    :target: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/actions
    :alt: GitHub Workflow CI Status

.. image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/code-style?label=Code%20Style&style=for-the-badge
    :target: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/actions
    :alt: GitHub Workflow Code Style Status

.. image:: https://img.shields.io/codecov/c/github/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
    :target: https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}

.. If you want the following badges to be visible, please remove this line, and unindent the lines below
    .. image:: https://img.shields.io/readthedocs/{{cookiecutter.project_slug}}/latest.svg?style=for-the-badge
        :target: https://{{cookiecutter.project_slug}}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

    .. image:: https://img.shields.io/pypi/v/{{cookiecutter.project_slug}}.svg?style=for-the-badge
        :target: https://pypi.org/project/{{cookiecutter.project_slug}}
        :alt: Python Package Index

    .. image:: https://img.shields.io/conda/vn/conda-forge/{{cookiecutter.project_slug}}.svg?style=for-the-badge
        :target: https://anaconda.org/conda-forge/{{cookiecutter.project_slug}}
        :alt: Conda Version


{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

Development
------------

For a development install, do the following in the repository directory:

.. code-block:: bash

    conda env update -f ci/environment.yml
    conda activate sandbox-devel
    python -m pip install -e .

Also, please install `pre-commit` hooks from the root directory of the created project by running::

      pre-commit install

These code style pre-commit hooks (black, isort, flake8, ...) will run every time you are about to commit code.

.. If you want the following badges to be visible, please remove this line, and unindent the lines below
    Re-create notebooks with Pangeo Binder
    --------------------------------------

    Try notebooks hosted in this repo on Pangeo Binder. Note that the session is ephemeral.
    Your home directory will not persist, so remember to download your notebooks if you
    made changes that you need to use at a later time!

    .. image:: https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=GCE+us-central1&color=blue&style=for-the-badge
        :target: https://binder.pangeo.io/v2/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/master?urlpath=lab
        :alt: Binder
