# Generated by Django 2.2.1 on 2019-06-11 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_access', '0015_auto_20190611_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='description',
        ),
    ]