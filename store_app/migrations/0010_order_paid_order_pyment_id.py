# Generated by Django 5.0.4 on 2024-05-10 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0009_order_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='pyment_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
