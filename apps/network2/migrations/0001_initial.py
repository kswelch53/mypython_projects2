# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-14 04:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('network1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accept', models.BooleanField(default=False)),
                ('ignore', models.BooleanField(default=False)),
                ('invitee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='was_invited', to='network1.User')),
                ('inviter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invited', to='network1.User')),
            ],
        ),
    ]
