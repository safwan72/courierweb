# Generated by Django 3.2 on 2021-04-27 19:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('App_Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Location',
                'db_table': 'Location',
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel_weight', models.IntegerField(default=0)),
                ('parcel_type', models.CharField(choices=[('F', 'Fragile'), ('L', 'Liquid')], max_length=1)),
                ('added_for_delivery', models.BooleanField(default=False)),
                ('parcel_deliver_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deliver_to', to='App_Main.location')),
            ],
            options={
                'verbose_name_plural': 'Parcel',
                'db_table': 'Parcel',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_invoice_id', models.CharField(max_length=10)),
                ('order_id', models.CharField(max_length=10, unique=True)),
                ('ordered', models.BooleanField(default=False)),
                ('merchant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='merchant', to='App_Login.merchant')),
                ('orderer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_orderer', to=settings.AUTH_USER_MODEL)),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parcel', to='App_Main.parcel')),
            ],
            options={
                'verbose_name_plural': 'Order Table',
                'db_table': 'Order Table',
            },
        ),
    ]
