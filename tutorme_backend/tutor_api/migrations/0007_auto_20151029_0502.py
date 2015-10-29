# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_api', '0006_auto_20151029_0500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.TextField(unique=True),
        ),
    ]
