# Generated by Django 4.1 on 2022-11-01 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_alter_task_taskid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='taskid',
        ),
    ]