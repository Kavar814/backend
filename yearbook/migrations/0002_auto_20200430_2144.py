# Generated by Django 3.0.5 on 2020-04-30 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstitutionYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('school_year', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_educator', models.BooleanField()),
                ('institution_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.InstitutionYear')),
                ('yearbook_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.YearbookUser')),
            ],
        ),
        migrations.RemoveField(
            model_name='facultyprofileyear',
            name='faculty_profile',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='institution',
        ),
        migrations.RemoveField(
            model_name='studentprofile',
            name='yearbook_user',
        ),
        migrations.RemoveField(
            model_name='studentprofileyear',
            name='student_profile',
        ),
        migrations.RenameModel(
            old_name='EducationalInstitution',
            new_name='Institution',
        ),
        migrations.DeleteModel(
            name='FacultyProfile',
        ),
        migrations.DeleteModel(
            name='FacultyProfileYear',
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
        migrations.DeleteModel(
            name='StudentProfileYear',
        ),
        migrations.AddField(
            model_name='institutionyear',
            name='institution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yearbook.Institution'),
        ),
    ]