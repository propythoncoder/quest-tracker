# Generated by Django 4.1 on 2022-11-01 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0022_remove_employee_task_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='task_end_date',
            field=models.CharField(default=True, max_length=30),
        ),
        migrations.AddField(
            model_name='employee',
            name='task_title',
            field=models.CharField(default=True, max_length=30),
        ),
    ]
