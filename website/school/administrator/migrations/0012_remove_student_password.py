# Generated by Django 2.0 on 2019-01-21 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0011_auto_20190119_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
