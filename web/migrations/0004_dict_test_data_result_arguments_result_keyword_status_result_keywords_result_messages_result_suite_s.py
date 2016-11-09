# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-11-08 02:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20161108_0921'),
    ]

    operations = [
        migrations.CreateModel(
            name='dict_test_data',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('dataContent', models.CharField(max_length=255)),
                ('dataName', models.CharField(max_length=255)),
                ('caseId', models.IntegerField(default=11)),
                ('groupID', models.IntegerField(default=11)),
            ],
        ),
        migrations.CreateModel(
            name='result_arguments',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('keyword_id', models.IntegerField(default=10)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='result_keyword_status',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('test_run_id', models.IntegerField(default=10)),
                ('keyword_id', models.IntegerField(default=10)),
                ('status', models.TextField()),
                ('elapsed', models.IntegerField(default=255)),
            ],
        ),
        migrations.CreateModel(
            name='result_keywords',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('suite_id', models.IntegerField(default=10)),
                ('test_id', models.IntegerField(default=10)),
                ('keyword_id', models.IntegerField(default=10)),
                ('name', models.TextField()),
                ('type', models.TextField()),
                ('timeout', models.TextField()),
                ('doc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='result_messages',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('keyword_id', models.IntegerField(default=10)),
                ('level', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='result_suite_status',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('test_run_id', models.IntegerField(default=10)),
                ('suite_id', models.IntegerField(default=10)),
                ('elapsed', models.IntegerField(default=255)),
                ('failed', models.IntegerField(default=3)),
                ('passed', models.IntegerField(default=3)),
                ('status', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='result_suites',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('suite_id', models.IntegerField(default=10)),
                ('xml_id', models.TextField()),
                ('name', models.TextField()),
                ('source', models.TextField()),
                ('doc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='result_tag_status',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('test_run_id', models.IntegerField(default=10)),
                ('name', models.TextField()),
                ('critical', models.IntegerField(default=1)),
                ('elapsed', models.IntegerField(default=255)),
                ('failed', models.IntegerField(default=3)),
                ('passed', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='result_tags',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('test_id', models.IntegerField(default=10)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='result_test_run_errors',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('test_run_id', models.IntegerField(default=10)),
                ('level', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='result_test_run_status',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('test_run_id', models.IntegerField(default=10)),
                ('name', models.TextField()),
                ('elapsed', models.IntegerField(default=255)),
                ('failed', models.IntegerField(default=3)),
                ('passed', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='result_test_runs',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('source_file', models.TextField()),
                ('started_at', models.DateTimeField(auto_now_add=True)),
                ('finished_at', models.DateTimeField(auto_now_add=True)),
                ('hash', models.TextField()),
                ('imported_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='result_test_status',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('test_run_id', models.IntegerField(default=10)),
                ('test_id', models.IntegerField(default=10)),
                ('status', models.TextField()),
                ('elapsed', models.IntegerField(default=255)),
            ],
        ),
        migrations.CreateModel(
            name='result_tests',
            fields=[
                ('id', models.IntegerField(default=11, primary_key=True, serialize=False)),
                ('suite_id', models.IntegerField(default=10)),
                ('xml_id', models.TextField()),
                ('name', models.TextField()),
                ('timeout', models.DateTimeField(auto_now_add=True)),
                ('doc', models.TextField()),
            ],
        ),
    ]
