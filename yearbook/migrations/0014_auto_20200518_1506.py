# Generated by Django 3.0.5 on 2020-05-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yearbook', '0013_auto_20200518_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='logo',
            field=models.ImageField(default='default_institution_logo.png', upload_to='logos'),
        ),
    ]