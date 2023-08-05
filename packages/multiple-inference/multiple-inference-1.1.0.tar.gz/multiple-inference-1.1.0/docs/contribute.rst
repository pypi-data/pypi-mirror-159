Contribute to Multiple Inference
================================

I want to make it as easy as possible to contribute to this package. Below are guidelines for a high-quality contribution. If you're struggling with any of these steps, please open an `issue <https://gitlab.com/dsbowen/conditional-inference/-/issues>`_.

How to contribute:

#. Create a branch in git with your changes.
#. Push your branch to GitLab and issue a pull request.
#. Discuss the pull request.
#. Iterate with me until I accept the pull request.

You can edit your branch in `Gitpod <https://gitpod.io/#https://gitlab.com/dsbowen/conditional-inference>`_ to use a pre-built virtual environment. To work locally, install the requirements and the package with:

.. code-block::

	$ pip install -r requirements.txt
	$ pip install -e .

A good pull request should:

#. Describe the motivation. What problem are you solving, and how do you solve it?
#. Use the `black <https://black.readthedocs.io/en/stable/>`_ coding style. Run ``make format`` from the root directory to automatically format your changes.
#. If you create a new function or method, or modify the arguments for an existing function or method, document your changes with `Google-style <https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html>`_ docstrings. I recommend using `autoDocstring <https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>`_ if working in visual studio code. You can set it to create Google-style docstrings automatically. autoDocstring is installed automatically in the Gitpod workspace. Build and test the docs by running ``make docs`` from the root directory. Then, run ``make docserve`` and open http://localhost:8020/ to preview the documentation changes.
#. Test your changes. Add tests in the ``tests`` directory. Run ``make test`` from the root directory to check that your tests pass. This command also creates a code coverage report. Run ``make testserve`` and open http://localhost:8080/ to view a detailed code coverage report.

Some features I would like to see:

#. Bayesian estimators with mixture priors, expecially a `spike-and-slab prior <http://mathursuhas.com/the-bayesian-observer/2017/1/7/spike-and-slab-priors>`_.
#. `Post-selection inference <https://caesarxvii.github.io/MSHD-book-and-datasets/post-selection-inference.html>`_.
#. A multivariate truncated normal implementation using exponential tilting methods. See `here <https://hal.inria.fr/hal-01240154/document>`_ and `here <https://arxiv.org/pdf/1603.04166.pdf>`_.