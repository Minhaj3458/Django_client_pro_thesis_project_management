# Generated by Django 4.1.2 on 2022-10-21 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_App', '0002_remove_student_profile_student_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_profile',
            name='is_student',
        ),
    ]
