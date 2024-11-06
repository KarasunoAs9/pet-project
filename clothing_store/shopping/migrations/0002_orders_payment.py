# Generated by Django 5.1.2 on 2024-11-06 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0001_initial'),
        ('shopping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveBigIntegerField(unique=True)),
                ('status', models.CharField(choices=[('In progres', 'In progres'), ('Delivery', 'Delivery'), ('Completed', 'Completed')], max_length=11)),
                ('added_to', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart', to='shopping.cart')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_number', models.CharField(max_length=19)),
                ('expiration_term', models.CharField(max_length=5)),
                ('cvv', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_auth.customer')),
            ],
        ),
    ]
