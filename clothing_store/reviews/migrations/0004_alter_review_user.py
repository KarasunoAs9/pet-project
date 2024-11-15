# Generated by Django 5.1.2 on 2024-11-07 10:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_auth', '0001_initial'),
        ('reviews', '0003_rename_reviews_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='app_auth.customer'),
        ),
    ]
