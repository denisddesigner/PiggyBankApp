# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 13:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companies', '0003_auto_20171124_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInvite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accepted', models.BooleanField(default=False)),
                ('uuid', models.CharField(default='', max_length=32)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='invites', to='companies.Company')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyinvite_created', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyinvite_received', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
