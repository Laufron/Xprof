# Generated by Django 2.2.1 on 2019-06-04 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_access', '0005_auto_20190531_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.SlugField(default='slug', max_length=100),
            preserve_default=False,
        ),
    ]
