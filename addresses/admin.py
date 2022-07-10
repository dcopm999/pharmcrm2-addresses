# -*- coding: utf-8 -*-
from django.contrib import admin

from addresses import models


@admin.register(models.Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name"]
    list_filter = ["country"]


@admin.register(models.Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ["name", "region"]
    search_fields = ["name"]
    list_filter = ["region"]


@admin.register(models.District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ["name", "area"]
    search_fields = ["name"]
    list_filter = ["area"]


@admin.register(models.Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ["name", "district"]
    search_fields = ["name"]
    list_filter = ["district"]
