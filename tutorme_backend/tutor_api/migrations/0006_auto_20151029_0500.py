# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_api', '0005_auto_20151029_0457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='major',
            field=models.ForeignKey(related_name='classes', to='tutor_api.Department', to_field=b'shortName'),
        ),
    ]
