# Generated by Django 4.2.5 on 2023-10-05 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_min_km_driven_pricingconfig_dbp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricingconfig',
            old_name='price_per_km',
            new_name='DAP',
        ),
        migrations.RenameField(
            model_name='pricingconfig',
            old_name='price_per_minute',
            new_name='TMF',
        ),
    ]
