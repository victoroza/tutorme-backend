# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
