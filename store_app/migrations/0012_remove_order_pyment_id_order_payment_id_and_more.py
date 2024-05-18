# Generated by Django 5.0.4 on 2024-05-11 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0011_alter_order_additional_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='pyment_id',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
