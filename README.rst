.. image:: https://img.shields.io/github/workflow/status/NCAR/cookiecutter-pypackage/CI?logo=github&style=for-the-badge
    :target: https://github.com/NCAR/cookiecutter-pypackage/actions
    :alt: GitHub Workflow CI Status

Cookiecutter PyPackage
======================

Custom Cookiecutter_ template for a Python package.


Features
--------

* Free software: Apache-2.0 license
* Pytest_ runner: Supports `pytest` style tests
* GitHub-Actions_: Ready for continuous integration testing using GitHub Actions
* Coverage_ : Code coverage with codecov.
* Pre-commit_ hooks: Code style pre-commit hooks (black, isort, flake8, ...) that will run every time you are about to commit code
* Auto-release to PyPI_ when you push a new tag to master (optional)

Usage
-----

Install the latest Cookiecutter if you haven't installed it yet (this requires Cookiecutter 1.4.0 or higher)::

    python -m pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/NCAR/cookiecutter-pypackage.git

Then:

* Create a git repo and push it to GitHub.
* Add the repo to your codecov.io account (optional)
* (Optional) install pre-commit hooks from the root directory of the created project by running::

      pip install pre-commit

      pre-commit install

* Release your package the standard Python way.


.. _GitHub-Actions: https://help.github.com/en/actions/
.. _Pytest: http://pytest.org/
.. _Coverage: https://codecov.io/
.. _Pre-commit: https://github.com/pre-commit/pre-commit-hooks
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _PyPI: https://pypi.org/
