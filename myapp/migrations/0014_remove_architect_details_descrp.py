# Generated by Django 4.1.7 on 2023-05-27 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_document'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='architect_details',
            name='descrp',
        ),
    ]
