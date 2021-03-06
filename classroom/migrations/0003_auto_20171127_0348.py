# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 03:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0002_auto_20171125_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('repo_url', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.IntegerField()),
                ('merge_branch', models.CharField(max_length=255)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='klass',
            name='admins',
            field=models.ManyToManyField(blank=True, related_name='admin_classes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='klass',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='student_classes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='assignment',
            name='klass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classroom.Klass'),
        ),
    ]
