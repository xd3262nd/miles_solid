# Generated by Django 2.2.5 on 2019-09-23 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miles_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miles',
            name='vehicle',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
