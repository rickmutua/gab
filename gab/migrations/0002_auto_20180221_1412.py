# Generated by Django 2.0.2 on 2018-02-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]