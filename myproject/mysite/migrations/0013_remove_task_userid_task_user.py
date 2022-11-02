# Generated by Django 4.1 on 2022-11-01 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mysite', '0012_alter_task_userid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='userid',
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
