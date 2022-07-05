# -*- coding: utf-8
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AddressesConfig(AppConfig):
    name = "addresses"
    verbose_name = _("addresses")
