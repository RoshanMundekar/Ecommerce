# Generated by Django 4.2.3 on 2024-06-11 11:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store_app", "0006_order_orderitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="paid",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="payment_id",
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="amount",
            field=models.CharField(max_length=100),
        ),
    ]
