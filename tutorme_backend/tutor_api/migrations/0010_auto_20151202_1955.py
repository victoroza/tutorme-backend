# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_api', '0009_auto_20151202_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appintment',
            name='tutee',
        ),
        migrations.RemoveField(
            model_name='appintment',
            name='tutor',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
