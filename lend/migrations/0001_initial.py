# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 09:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import lend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=255)),
                ('book_author', models.CharField(max_length=255)),
                ('book_cover', models.ImageField(help_text='Book Cover', upload_to=lend.models.PathAndRename('/covers'), verbose_name='Book Cover')),
                ('book_edition', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='book_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='lend.Category'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_genre',
            field=models.ManyToManyField(blank=True, to='lend.Genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='book_lender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
