.. image:: https://img.shields.io/circleci/project/github/NCAR/cookiecutter-pypackage/master.svg?style=for-the-badge
    :target: https://circleci.com/gh/NCAR/cookiecutter-pypackage/tree/master

Cookiecutter-pypackage
======================

Custom cookiecutter template for a Python package.


* Free software: Apache-2.0 license
* Pytest_ runner: Supports `unittest`, `pytest`, `nose` style tests and more
* Circle-CI_: Ready for CircleCI Continuous integration testing
* Coverage_ : Code coverage with codecov.
* Tox_ testing: Setup to easily test for python 2.7, 3.6, and 3.7.
* Sphinx_ docs: Documentation raedy for generation with, for example, ReadTheDocs_
* Pre-commit_ hooks: Code style pre-commit hooks (balck, isort, flake8, ...) that will run every time you are about to commit code
* Wheel_ support: Use the newest python package distribution standard from the get go

Usage
-----

Generate a Python package project::

    cookiecutter https://github.com/NCAR/cookiecutter-pypackage.git

Then:

* Create a repo and put it there.
* Add the repo to your Circle CI account.
* Add the repo to your codecov.io account (optional)
* (Optional) install pre-commit hooks from the root directory of the created project by running::
  
  pip install pre-commit
  pre-commit install
  
* Add the repo to your ReadTheDocs account + turn on the ReadTheDocs service hook.
* Run `tox` to make sure all tests pass.
* Release your package the standard Python way.


.. _Circle-CI: https://circleci.com/dashboard
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.org/
.. _Pytest: http://pytest.org/
.. _Wheel: http://pythonwheels.com
.. _Coverage: https://codecov.io/
.. _Pre-commit: https://github.com/pre-commit/pre-commit-hooks
