# Generated by Django 3.1.3 on 2020-11-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Matkul',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matakuliah', models.CharField(max_length=200)),
                ('dosen', models.CharField(max_length=100)),
                ('hari', models.CharField(max_length=50)),
                ('jam', models.CharField(max_length=20)),
            ],
        ),
    ]
