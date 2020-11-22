# Generated by Django 3.0.11 on 2020-11-22 10:33

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PartyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('create_date', models.DateTimeField(default=datetime.datetime(2020, 11, 22, 11, 33, 24, 852495))),
                ('adress', models.CharField(max_length=130)),
                ('free_space', models.SmallIntegerField(null=True)),
                ('description', models.TextField(max_length=200)),
                ('name', models.TextField(max_length=75, null=True)),
                ('party_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='partee.PartyType')),
            ],
        ),
    ]
