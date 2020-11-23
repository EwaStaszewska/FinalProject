# Generated by Django 3.0.10 on 2020-11-23 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('name', models.TextField(max_length=75, null=True)),
                ('city', models.CharField(max_length=50)),
                ('free_space', models.SmallIntegerField(null=True)),
                ('description', models.TextField(max_length=100)),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('party_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='partee.PartyType')),
            ],
        ),
    ]
