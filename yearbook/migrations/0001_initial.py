# Generated by Django 3.0.5 on 2020-04-30 20:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalInstitution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=30)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.EducationalInstitution')),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_year', models.CharField(max_length=30)),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.EducationalInstitution')),
            ],
        ),
        migrations.CreateModel(
            name='YearbookUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(max_length=140)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentProfileYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=30)),
                ('quote', models.TextField(max_length=140)),
                ('student_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.StudentProfile')),
            ],
        ),
        migrations.AddField(
            model_name='studentprofile',
            name='yearbook_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.YearbookUser'),
        ),
        migrations.CreateModel(
            name='FacultyProfileYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=30)),
                ('quote', models.TextField(max_length=140)),
                ('faculty_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.FacultyProfile')),
            ],
        ),
        migrations.AddField(
            model_name='facultyprofile',
            name='yearbook_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.YearbookUser'),
        ),
    ]
