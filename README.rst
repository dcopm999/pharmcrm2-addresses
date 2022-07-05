=============================
PharmCRM2 Addresses
=============================

.. image:: https://badge.fury.io/py/pharmcrm2-addresses.svg
    :target: https://badge.fury.io/py/pharmcrm2-addresses

.. image:: https://travis-ci.org/dcopm999/pharmcrm2-addresses.svg?branch=master
    :target: https://travis-ci.org/dcopm999/pharmcrm2-addresses

.. image:: https://codecov.io/gh/dcopm999/pharmcrm2-addresses/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/dcopm999/pharmcrm2-addresses

PharmCRM2 Addresses

Documentation
-------------

The full documentation is at https://pharmcrm2-addresses.readthedocs.io.

Quickstart
----------

Install PharmCRM2 Addresses::

    pip install pharmcrm2-addresses

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'addresses',
        ...
    )

Add PharmCRM2 Addresses's URL patterns:

.. code-block:: python

    urlpatterns = [
        ...
        path('addresses/', include('addresses.urls')),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox


Development commands
---------------------

::

    pip install -r requirements_dev.txt
    invoke -l


Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
