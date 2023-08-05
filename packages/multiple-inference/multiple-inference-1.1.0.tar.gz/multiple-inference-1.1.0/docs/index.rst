.. Conditional Inference documentation master file, created by
   sphinx-quickstart on Mon Nov 12 14:17:27 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Multiple Inference documentation
================================

A statistics package for comparing multiple parameters (e.g., multiple treatments, policies, or subgroups).

.. image:: https://readthedocs.org/projects/dsbowen-conditional-inference/badge/?version=latest
   :target: https://dsbowen-conditional-inference.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status
.. image:: https://joss.theoj.org/papers/7a2a4af277c0ad6ad6f41897f4489888/status.svg
   :target: https://joss.theoj.org/papers/7a2a4af277c0ad6ad6f41897f4489888
.. image:: https://gitlab.com/dsbowen/conditional-inference/badges/master/pipeline.svg
   :target: https://gitlab.com/dsbowen/conditional-inference/-/commits/master
.. image:: https://gitlab.com/dsbowen/conditional-inference/badges/master/coverage.svg
   :target: https://gitlab.com/dsbowen/conditional-inference/-/commits/master
.. image:: https://badge.fury.io/py/conditional-inference.svg
   :target: https://badge.fury.io/py/conditional-inference
.. image:: https://img.shields.io/badge/License-MIT-brightgreen.svg
   :target: https://gitlab.com/dsbowen/conditional-inference/-/blob/master/LICENSE
.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gl/dsbowen%2Fconditional-inference/HEAD?urlpath=lab
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black

|
Statement of need
=================

Researchers often compare many "things" simultaneously. Policymakers regularly compare the effects of many possible policy decisions. Psychologists study individual differences by comparing many people. Diversity researchers compare many demographic groups. Economists compare states and countries in terms of economic variables. Geneticists search for correlations among many genes and phenotypic traits.

We designed this package to help practitioners quickly, easily, and accurately perform such comparisons. It uses a ``statsmodels``-like API and provides template notebooks for ease of use. In just a few clicks, you can upload a ``.csv`` file of conventional estimates (e.g., ordinary least squares or instrumental variables estimates) to a Jupyter binder and click "run" to apply a suite of multiple inference tools to your data.

Motivation
==========

Multiple inference techniques outperform standard methods like ordinary least squares (OLS) and instrumental variables (IV) estimation for comparing multiple parameters. `This example <examples/bayes_primer.html>`_ shows how to apply Bayesian estimators to a randomized control trial testing many interventions to increase vaccination rates.

Start here
==========

The "Multiple Inference Cookbook" allows you to apply a suite of multiple inference tools to your data without writing a single line of code. Click `here <examples/multiple_inference.html>`_ to see the cookbook, or click the badge below to launch a Jupyter binder and apply the cookbook to your data.

.. image:: https://mybinder.org/badge_logo.svg
   :target: https://mybinder.org/v2/gl/dsbowen%2Fconditional-inference/HEAD?urlpath=lab/tree/docs/examples/multiple_inference.ipynb

|
Installation
============

Install the latest stable build.

.. code-block::

   $ pip install multiple-inference

Install the latest dev build.

.. code-block::

   $ pip install git+https://gitlab.com/dsbowen/conditional-inference.git

Issues
======

Please submit issues `here <https://gitlab.com/dsbowen/conditional-inference/-/issues>`_.

Contents
========

.. toctree::
   :maxdepth: 2

   api/index
   examples/index
   Contribute <contribute>
   Changelog <changelog>

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Citations
=========

.. code-block::

   @software(multiple-inference,
      title={ Multiple Inference },
      author={ Bowen, Dillon },
      year={ 2022 },
      url={ https://dsbowen-conditional-inference.readthedocs.io/en/latest/?badge=latest }
   )

Acknowledgements
================

I would like to thank Isaiah Andrews, Toru Kitagawa, Adam McCloskey, and Jeff Rowley for invaluable feedback on my early drafts.

My issue templates are based on the `statsmodels <https://github.com/statsmodels/statsmodels/issues/new/choose>`_ issue templates.