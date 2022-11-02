# Generated by Django 4.1 on 2022-11-01 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0029_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('employee_id', models.CharField(max_length=30)),
                ('employee_name', models.CharField(max_length=30)),
                ('task_title', models.CharField(max_length=30)),
                ('task_end_date', models.CharField(max_length=30)),
                ('upload_task', models.FileField(upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='task_end_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='task_title',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='upload_task',
        ),
    ]