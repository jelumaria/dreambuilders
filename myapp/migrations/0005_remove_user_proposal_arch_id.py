# Generated by Django 4.1.7 on 2023-05-03 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_architect_details_architect_plans_plan_details_plan_settings_sales_master_user_proposal_user_rating_'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_proposal',
            name='arch_id',
        ),
    ]