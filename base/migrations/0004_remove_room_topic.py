# Generated by Django 5.0.3 on 2024-03-28 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_room_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='topic',
        ),
    ]
