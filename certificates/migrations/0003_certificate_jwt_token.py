# Generated by Django 4.2.6 on 2023-10-15 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0002_remove_student_teachers_alter_teacher_students'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='jwt_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]