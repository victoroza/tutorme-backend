# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutor_api', '0007_auto_20151029_0502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appintment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateTimeField()),
                ('location', models.TextField()),
                ('notes', models.TextField()),
                ('aClass', models.ForeignKey(related_name='appointments', to='tutor_api.Class')),
                ('tutee', models.ForeignKey(related_name='appointments_tutee', to='tutor_api.User')),
                ('tutor', models.ForeignKey(related_name='appointments_tutor', to='tutor_api.User')),
            ],
        ),
    ]
