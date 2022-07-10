# -*- coding: utf-8 -*-
from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from slugify import slugify


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name=_("Country name"))
    name_eng = models.CharField(
        max_length=30, unique=True, blank=True, verbose_name=_("Country name english")
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")

    def get_absolute_url(self):
        return reverse("addresses:country-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super().save(*args, **kwargs)


class Region(models.Model):
    country = models.ForeignKey(
        Country,
        on_delete=models.PROTECT,
        verbose_name=_("Country"),
    )
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Region name"))
    name_eng = models.CharField(
        max_length=100, unique=True, blank=True, verbose_name=_("Region name english")
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")

    def get_absolute_url(self):
        return reverse("addresses:region-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.country}, {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super().save(*args, **kwargs)


class Area(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
        verbose_name=_("Region"),
    )
    name = models.CharField(
        max_length=100, unique=True, verbose_name=_("District name")
    )
    name_eng = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("District name english"),
        blank=True,
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("Area")
        verbose_name_plural = _("Areas")

    def get_absolute_url(self):
        return reverse("addresses:district-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.region}, {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class District(models.Model):
    area = models.ForeignKey(
        Area,
        on_delete=models.CASCADE,
        verbose_name=_("Area"),
    )
    name = models.CharField(
        max_length=100, unique=True, verbose_name=_("District name")
    )
    name_eng = models.CharField(
        max_length=100,
        verbose_name=_("District name english"),
        blank=True,
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("District")
        verbose_name_plural = _("Districts")

    def get_absolute_url(self):
        return reverse("addresses:district-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.region}, {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Street(models.Model):
    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        verbose_name=_("Desctrict"),
    )
    name = models.CharField(max_length=100, unique=True, verbose_name=_("Street name"))
    name_eng = models.CharField(
        max_length=100,
        verbose_name=_("Street name english"),
        blank=True,
    )
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    class Meta:
        verbose_name = _("Street")
        verbose_name_plural = _("Streets")

    def get_absolute_url(self):
        return reverse("addresses:street-detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f"{self.district}, {self.name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class OKATO(models.Model):
    region = models.PositiveIntegerField(
        validators=[
            validators.RegexValidator(
                regex=r"^\d{2}$", message=_("Region code must be 2 numbers")
            )
        ],
        verbose_name=_("Region code"),
    )
    area = models.PositiveIntegerField(
        validators=[
            validators.RegexValidator(
                regex=r"^\d{3}$", message=_("Area/City code must be 3 numbers")
            )
        ],
        verbose_name=_("Area/City code"),
    )
    district = models.IntegerField(
        validators=[
            validators.RegexValidator(
                regex=r"^\d{3}$", message=_("District code must be 3 numbers")
            )
        ],
        null=True,
        verbose_name=_("District code"),
    )
    rural = models.IntegerField(
        validators=[
            validators.RegexValidator(
                regex=r"^\d{3}$", message=_("Rural locality code must be 3 numbers")
            )
        ],
        null=True,
        verbose_name=_("Rural locality"),
    )
    section = models.PositiveIntegerField(
        validators=[
            validators.RegexValidator(
                regex=r"^\d{1}$", message=_("Section code must be 1 numbers")
            )
        ],
        verbose_name=_("Section code"),
    )
    name = models.CharField(max_length=250, verbose_name=_("Name of the territory"))
    additional_info = models.CharField(
        max_length=80, blank=True, verbose_name=_("Additional information")
    )
    desc = models.TextField(blank=True, verbose_name=_("Description"))
    document_num = models.IntegerField(
        validators=[
            validators.RegexValidator(
                regex=r"^\d{3}$", message=_("Document number must be 3 numbers")
            )
        ],
        null=True,
        verbose_name=_("Document number"),
    )
    document_type = models.IntegerField(
        validators=[
            validators.RegexValidator(
                regex=r"^\d{1}$", message=_("Document type must be 1 numbers")
            )
        ],
        null=True,
        verbose_name=_("Document type"),
    )
    date_acceptance = models.DateField(verbose_name=_("Date of acceptance"))
    date_introduction = models.DateField(verbose_name=_("Date of introduction"))
    slug = models.SlugField(
        max_length=140,
        db_index=True,
        blank=True,
        editable=False,
        verbose_name=_("slug"),
    )
    created = models.DateTimeField(
        auto_now_add=True, editable=False, verbose_name=_("Created")
    )
    updated = models.DateTimeField(
        auto_now=True, editable=False, verbose_name=_("Updated")
    )

    def __str__(self):
        return f"{self.name} ({self.region}-{self.area}-{self.district}-{self.rural}-{self.section})"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.__str__())
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _("OKATO")
        verbose_name_plural = _("OKATO")
