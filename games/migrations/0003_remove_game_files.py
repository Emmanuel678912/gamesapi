# Generated by Django 3.1.7 on 2021-05-07 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_game_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='files',
        ),
    ]
