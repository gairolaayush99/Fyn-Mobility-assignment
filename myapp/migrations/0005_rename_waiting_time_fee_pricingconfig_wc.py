# Generated by Django 4.2.5 on 2023-10-05 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_price_per_km_pricingconfig_dap_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pricingconfig',
            old_name='waiting_time_fee',
            new_name='WC',
        ),
    ]