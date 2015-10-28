# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_api', '0002_auto_20151028_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='shortName',
            field=models.CharField(unique=True, max_length=10),
        ),
    ]
