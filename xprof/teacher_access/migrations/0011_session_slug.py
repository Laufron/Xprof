# Generated by Django 2.2.1 on 2019-06-06 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_access', '0010_session_number_eval'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
