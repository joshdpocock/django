# Generated by Django 2.1.2 on 2018-10-26 11:38

import DMA.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DMA', '0002_auto_20181026_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='area_6_dmas',
            name='leakage',
            field=models.IntegerField(default=DMA.models.random_int),
        ),
    ]
