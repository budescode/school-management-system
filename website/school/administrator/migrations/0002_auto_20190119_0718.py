# Generated by Django 2.0 on 2019-01-19 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalresult',
            name='grade',
            field=models.CharField(max_length=3),
        ),
    ]
