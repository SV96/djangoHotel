# Generated by Django 3.0.4 on 2020-04-19 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20200419_0953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='property',
            name='category',
        ),
    ]