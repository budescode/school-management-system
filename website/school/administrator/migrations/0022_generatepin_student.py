# Generated by Django 2.0 on 2019-01-27 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0021_generatepin'),
    ]

    operations = [
        migrations.AddField(
            model_name='generatepin',
            name='student',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='administrator.Student'),
            preserve_default=False,
        ),
    ]
