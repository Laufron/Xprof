# Generated by Django 2.2.1 on 2019-05-30 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('login', models.CharField(default='login', max_length=100)),
                ('password', models.CharField(default='azerty', max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_access.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_access.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concerned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_access.User')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_access.Session')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher_access.Skill')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='professors',
            field=models.ManyToManyField(blank=True, related_name='courses_given', to='teacher_access.User'),
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_followed', to='teacher_access.User'),
        ),
    ]
