.. image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/CI?logo=github&style=for-the-badge
    :target: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/actions
    :alt: GitHub Workflow CI Status

.. image:: https://img.shields.io/github/workflow/status/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/code-style?label=Code%20Style&style=for-the-badge
    :target: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/actions
    :alt: GitHub Workflow Code Style Status

.. image:: https://img.shields.io/codecov/c/github/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}.svg?style=for-the-badge
    :target: https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}

{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

Development
------------

For a development install, do the following in the repository directory:

.. code-block:: bash

    conda env update -f ci/environment.yml
    conda activate sandbox-devel
    python -m pip install -e .


Re-create notebooks with Pangeo Binder
--------------------------------------

Try these notebooks on Pangeo Binder. Note that the session is ephemeral.
Your home directory will not persist, so remember to download your notebooks if you
made changes that you need to use at a later time!

.. image:: https://img.shields.io/static/v1.svg?logo=Jupyter&label=Pangeo+Binder&message=GCE+us-central1&color=blue&style=for-the-badge
    :target: https://binder.pangeo.io/v2/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.project_slug}}/master?urlpath=lab
    :alt: Binder
