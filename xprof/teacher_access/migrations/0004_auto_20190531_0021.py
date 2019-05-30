# Generated by Django 2.2.1 on 2019-05-30 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher_access', '0003_evaluation_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('login', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': 'Student',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('login', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=50)),
            ],
            options={
                'verbose_name': 'Teacher',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(blank=True, related_name='courses_given', to='teacher_access.Teacher'),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_followed', to='teacher_access.Student'),
        ),
        migrations.AlterField(
            model_name='evaluation',
            name='concerned',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_access.Student'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]