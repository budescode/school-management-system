# Generated by Django 2.0 on 2019-01-30 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0036_auto_20190130_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='generalresult',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
