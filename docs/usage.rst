=====
Usage
=====

To use PharmCRM2 Addresses in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'addresses.apps.AddressesConfig',
        ...
    )

Add PharmCRM2 Addresses's URL patterns:

.. code-block:: python

    from addresses import urls as addresses_urls


    urlpatterns = [
        ...
        url(r'^', include(addresses_urls)),
        ...
    ]
