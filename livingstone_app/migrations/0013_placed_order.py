# Generated by Django 5.2.3 on 2025-07-09 12:49

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livingstone_app', '0012_cartitem_address_cartitem_availability_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Placed_Order',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Deliverd', 'Deliverd'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50)),
                ('price', models.FloatField(blank=True, null=True)),
                ('payment_status', models.IntegerField(choices=[(1, 'Success'), (2, 'Failed'), (3, 'Pending')], default=3)),
                ('product_id_number', models.CharField(blank=True, default=None, max_length=255, null=True, unique=True)),
                ('order_id', models.CharField(blank=True, default=None, max_length=10000000, null=True)),
                ('datetime_of_payment', models.DateTimeField(default=django.utils.timezone.now)),
                ('transaction_id', models.CharField(blank=True, max_length=10000000, null=True)),
                ('mihpayid', models.CharField(blank=True, max_length=10000000, null=True)),
                ('hash', models.CharField(blank=True, max_length=10000000, null=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livingstone_app.address')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='livingstone_app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
