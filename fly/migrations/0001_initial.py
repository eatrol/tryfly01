# Generated by Django 3.1.2 on 2022-12-31 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dbfly',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('check', models.CharField(max_length=50)),
                ('memo', models.CharField(max_length=100)),
                ('phase', models.CharField(max_length=50)),
                ('lesson', models.CharField(max_length=100)),
            ],
        ),
    ]
