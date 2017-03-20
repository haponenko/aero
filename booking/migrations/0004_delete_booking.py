# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20151213_1945'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
