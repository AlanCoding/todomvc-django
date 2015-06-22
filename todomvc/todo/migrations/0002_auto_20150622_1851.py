# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='text',
            new_name='title',
        ),
        migrations.AddField(
            model_name='item',
            name='order',
            field=models.IntegerField(null=True),
        ),
    ]
