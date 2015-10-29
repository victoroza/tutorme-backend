# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_api', '0004_class_school'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='major',
            field=models.ForeignKey(related_name='classes', to='tutor_api.Department'),
        ),
        migrations.AlterField(
            model_name='class',
            name='school',
            field=models.ForeignKey(related_name='classes', to='tutor_api.School'),
        ),
    ]
