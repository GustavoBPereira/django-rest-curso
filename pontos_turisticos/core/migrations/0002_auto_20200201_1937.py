# Generated by Django 3.0.2 on 2020-02-01 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristspot',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
