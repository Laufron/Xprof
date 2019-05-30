# Generated by Django 2.2.1 on 2019-05-30 17:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_access', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['name'], 'verbose_name': 'Course'},
        ),
        migrations.AlterModelOptions(
            name='evaluation',
            options={'ordering': ['skill'], 'verbose_name': 'evaluation'},
        ),
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['date'], 'verbose_name': 'session'},
        ),
        migrations.AlterModelOptions(
            name='skill',
            options={'ordering': ['name'], 'verbose_name': 'skill'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['name'], 'verbose_name': 'Teacher/Student'},
        ),
        migrations.AlterField(
            model_name='skill',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_access.Course', verbose_name='evaluated in'),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('T', 'teacher'), ('S', 'student')], default='T', max_length=50),
        ),
    ]
