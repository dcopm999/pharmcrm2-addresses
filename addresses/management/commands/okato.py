import csv
import os
import ssl
from datetime import datetime

import wget
from django.conf import settings
from django.core.management.base import BaseCommand

from addresses import models


class Command(BaseCommand):
    help = "Import soato"
    okato_url = "https://rosstat.gov.ru/opendata/7708234640-okato/data-20220627-structure-20140709.csv"
    OUTPUT_DIR = os.path.join(settings.MEDIA_ROOT, "okato")
    CSV_FILE = os.path.join(OUTPUT_DIR, okato_url.split("/")[-1])

    def handle(self, *args, **options):
        self._download(self.okato_url)
        items = self._parse_csv(self.CSV_FILE)
        titles = [
            "region",
            "area",
            "district",
            "rural",
            "section",
            "name",
            "additional_info",
            "desc",
            "document_num",
            "document_type",
            "date_acceptance",
            "date_introduction",
        ]
        for item in items:
            dict_item = dict(zip(titles, item))
            dict_item["date_acceptance"] = datetime.strptime(
                dict_item["date_acceptance"], "%d.%m.%Y"
            ).date()
            dict_item["date_introduction"] = datetime.strptime(
                dict_item["date_introduction"], "%d.%m.%Y"
            ).date()
            models.OKATO.objects.update_or_create(**dict_item)
        self.stdout.write(self.style.SUCCESS("Success"))

    def _parse_csv(self, csv_file):
        result = []
        with open(csv_file, encoding="windows-1251") as f:
            csv_file = csv.reader(f, delimiter=";")
            for item in csv_file:
                result.append(item)
        return result

    def _download(self, url: str) -> str:
        ssl._create_default_https_context = ssl._create_unverified_context
        FILENAME = url.split("/")[-1]
        RESULT_FILE = os.path.join(self.OUTPUT_DIR, FILENAME)

        if not os.path.exists(self.OUTPUT_DIR):
            os.makedirs(self.OUTPUT_DIR)
            self.stdout.write(
                self.style.SUCCESS(
                    "Created output dir: %s" % os.path.abspath(self.OUTPUT_DIR)
                )
            )
        if os.path.isfile(RESULT_FILE):
            os.remove(RESULT_FILE)
            self.stdout.write(self.style.SUCCESS("Removed old file: %s" % RESULT_FILE))
        self.stdout.write(self.style.SUCCESS("Downloading file form url: %s" % url))
        wget.download(url, RESULT_FILE)
        self.stdout.write(self.style.SUCCESS("\tSuccess"))
        return RESULT_FILE
