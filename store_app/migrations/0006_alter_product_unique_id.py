# Generated by Django 5.0.4 on 2024-05-08 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0005_alter_product_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unique_id',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
