# Generated by Django 2.1.5 on 2020-04-28 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='spectatedcoordinates',
            name='bomb_count',
            field=models.IntegerField(default=-1),
        ),
    ]
