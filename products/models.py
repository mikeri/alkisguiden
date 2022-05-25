from django.db import models


class Product(models.Model):
    def __str__(self):
        return self.name

    code = models.CharField(max_length=64)
    name = models.CharField(max_length=256)
    url = models.CharField(max_length=256)
    alcohol = models.FloatField()
    price = models.FloatField()
    litre_price = models.FloatField()
    alcohol_litre_price = models.FloatField()
    volume = models.FloatField()
    type = models.ForeignKey("ProductType", on_delete=models.PROTECT)

    def calculate(self):
        self.litre_price = self.price / self.volume
        if self.alcohol:
            self.alcohol_litre_price = self.litre_price / self.alcohol
        else:
            self.alcohol_litre_price = 0

    def save(self, *args, **kwargs):
        self.calculate()
        super().save(*args, **kwargs)


class ProductType(models.Model):
    def __str__(self):
        return self.name

    name = models.CharField(max_length=64)


class Slogan(models.Model):
    def __str__(self):
        return self.text

    text = models.CharField(max_length=256)
