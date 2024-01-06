from django.core.management.base import BaseCommand, CommandError
from products import models
import json


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("product_file", help="JSON file with products")

    def handle(self, **options):
        with open(options["product_file"], "r") as fobj:
            products = json.load(fobj)
        new = 0
        exsisting = 0
        for import_product in products:
            if (
                not import_product.get("alcohol")
                or import_product["alcohol"]["value"] == 0
            ):
                continue
            try:
                category = import_product.get("main_sub_category")
                if category is not None:
                    category = category["name"]
                if not category:
                    category = import_product["main_category"]["name"]
                if category.startswith("Alkoholfri"):
                    continue
                product, created = models.Product.objects.get_or_create(
                    code=str(import_product["code"]),
                    defaults={
                        "name": import_product["name"],
                        "url": import_product["url"],
                        "price": import_product["price"]["value"],
                        "volume": import_product["volume"]["value"],
                        "alcohol": import_product["alcohol"]["value"],
                        "type": models.ProductType.objects.get_or_create(name=category)[
                            0
                        ],
                    },
                )
                if created:
                    new += 1
                else:
                    exsisting += 1
            except KeyError:
                print("Skipped:")
                print(import_product)
        print(f"Imported {new + exsisting} products, {new} newly created")
