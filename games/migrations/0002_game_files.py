# Generated by Django 3.1.7 on 2021-04-30 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='files',
            field=models.FileField(blank=True, upload_to='files/'),
        ),
    ]
