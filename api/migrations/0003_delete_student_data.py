# Generated by Django 4.1.13 on 2024-04-20 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_student_data_delete_mymodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='student_data',
        ),
    ]
