# Generated by Django 2.0 on 2019-01-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0019_auto_20190123_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='total_course',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
