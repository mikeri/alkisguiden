from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=64)),
                ("name", models.CharField(max_length=256)),
                ("url", models.CharField(max_length=256)),
                ("alcohol", models.FloatField()),
                ("price", models.FloatField()),
                ("litre_price", models.FloatField()),
                ("alcohol_litre_price", models.FloatField()),
                ("volume", models.FloatField()),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="products.producttype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Slogan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.CharField(max_length=256)),
            ],
        ),
    ]
