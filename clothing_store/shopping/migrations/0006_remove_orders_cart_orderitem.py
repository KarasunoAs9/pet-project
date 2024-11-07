# Generated by Django 5.1.2 on 2024-11-06 14:25

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0005_alter_orders_number_alter_orders_status'),
        ('store', '0006_rename_size_productsize_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='cart',
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=4)),
                ('quantity', models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(10)])),
                ('added_to', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopping.orders')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
            ],
        ),
    ]