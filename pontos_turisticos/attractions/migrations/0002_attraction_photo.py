# Generated by Django 3.0.2 on 2020-02-03 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='tourist_sposts'),
        ),
    ]