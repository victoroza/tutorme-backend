# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_api', '0003_auto_20151028_0255'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='school',
            field=models.OneToOneField(related_name='classes', default=1, to='tutor_api.School'),
            preserve_default=False,
        ),
    ]
