# Generated by Django 5.0.4 on 2024-05-13 00:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
    ]