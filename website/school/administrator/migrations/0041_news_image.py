# Generated by Django 2.0 on 2019-02-08 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0040_gallery'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.FileField(default='media', upload_to=''),
        ),
    ]
