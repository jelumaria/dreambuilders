# Generated by Django 4.1.7 on 2023-05-31 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_delete_document_remove_user_proposal_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_proposal',
            name='status',
            field=models.CharField(max_length=25, null=True),
        ),
    ]