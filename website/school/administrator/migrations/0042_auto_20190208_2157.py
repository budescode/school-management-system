# Generated by Django 2.0 on 2019-02-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0041_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]