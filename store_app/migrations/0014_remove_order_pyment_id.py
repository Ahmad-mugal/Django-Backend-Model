# Generated by Django 5.0.4 on 2024-05-17 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0013_rename_payment_id_order_pyment_id_alter_order_paid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pyment_id',
        ),
    ]
