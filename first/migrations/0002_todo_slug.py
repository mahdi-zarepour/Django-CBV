# Generated by Django 3.2.8 on 2021-10-11 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
