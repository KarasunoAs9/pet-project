# Generated by Django 5.1.2 on 2024-11-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_productsize_quantity_alter_product_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productsize',
            name='quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]