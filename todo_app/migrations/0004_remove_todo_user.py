# Generated by Django 4.1.6 on 2023-02-17 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0003_todo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='user',
        ),
    ]