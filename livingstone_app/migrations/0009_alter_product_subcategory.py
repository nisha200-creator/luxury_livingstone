# Generated by Django 5.1.7 on 2025-07-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livingstone_app', '0008_alter_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(choices=[('tshirt', 'T-Shirt'), ('wallet', 'Wallet'), ('belt_men', 'Belt'), ('bag', 'Bag'), ('women_belt', 'Women Belt'), ('accessory_belt', 'Belt'), ('accessory_wallet', 'Wallet'), ('accessory_caps', 'Caps'), ('accessory_beer_mug', 'Beer Mug'), ('candles', 'Candles')], max_length=30),
        ),
    ]
