# Generated by Django 4.1 on 2022-11-01 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0028_delete_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.IntegerField()),
                ('department_name', models.CharField(max_length=30)),
                ('employee_name', models.CharField(max_length=30)),
                ('employee_email', models.CharField(max_length=30)),
                ('employee_address', models.CharField(max_length=30)),
                ('employee_doj', models.CharField(max_length=30)),
                ('profile', models.ImageField(upload_to='')),
                ('task_title', models.CharField(max_length=30)),
                ('task_end_date', models.CharField(max_length=30)),
                ('upload_task', models.FileField(upload_to='')),
                ('status', models.BooleanField(default=False)),
                ('added_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_on', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
