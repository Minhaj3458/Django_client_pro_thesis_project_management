# Generated by Django 4.1.2 on 2022-10-25 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_dashboard_App', '0002_user_student_id_user_teacher_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='teacher_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
