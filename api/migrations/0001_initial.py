# Generated by Django 2.1.5 on 2019-01-16 07:02

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('RED', 'RED'), ('WHITE', 'WHITE'), ('BLUE', 'BLUE')], default='RED', max_length=5)),
                ('my_field', multiselectfield.db.fields.MultiSelectField(choices=[('item_key1', 'Item title 1.1'), ('item_key2', 'Item title 1.2'), ('item_key3', 'Item title 1.3'), ('item_key4', 'Item title 1.4'), ('item_key5', 'Item title 1.5')], max_length=49)),
            ],
            options={
                'db_table': 'color',
            },
        ),
        migrations.CreateModel(
            name='RandomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_number', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=3)),
                ('code', models.UUIDField(unique=True)),
            ],
            options={
                'db_table': 'randomuser',
            },
        ),
        migrations.CreateModel(
            name='RandomUserManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_number', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='StudentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('student_code', models.CharField(max_length=10)),
                ('detail_data', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
