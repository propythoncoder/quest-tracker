# Generated by Django 4.1 on 2022-11-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0011_task_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='userid',
            field=models.IntegerField(),
        ),
    ]