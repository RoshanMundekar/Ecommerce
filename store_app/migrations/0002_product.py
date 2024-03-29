# Generated by Django 4.2.2 on 2023-06-21 17:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("store_app", "0001_initial"),
    ]

    operations = [
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
                (
                    "Uniqe_id",
                    models.CharField(
                        blank=True, max_length=200, null=True, unique=True
                    ),
                ),
                ("image", models.ImageField(upload_to="Product_image/img")),
                ("price", models.IntegerField()),
                (
                    "condition",
                    models.CharField(
                        choices=[("New", "New"), ("Old", "Old")], max_length=100
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("Information", models.CharField(max_length=2048)),
                ("description", models.TextField()),
                (
                    "stock",
                    models.CharField(
                        choices=[
                            ("IN STOCKS", "IN STOCKS"),
                            ("OUT OF STOCKS", "OUT OF STOCKS"),
                        ],
                        max_length=200,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("Publish", "Publish"), ("Drafts", "Drafts")],
                        max_length=200,
                    ),
                ),
                (
                    "created_date",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                (
                    "brand",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store_app.brand",
                    ),
                ),
                (
                    "categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store_app.categories",
                    ),
                ),
                (
                    "color",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store_app.color",
                    ),
                ),
                (
                    "filter_price",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="store_app.filter_price",
                    ),
                ),
            ],
        ),
    ]
