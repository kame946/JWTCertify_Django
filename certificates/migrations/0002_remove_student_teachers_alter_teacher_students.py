# Generated by Django 4.2.6 on 2023-10-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='teachers',
        ),
        migrations.AlterField(
            model_name='teacher',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='teachers', to='certificates.student'),
        ),
    ]
