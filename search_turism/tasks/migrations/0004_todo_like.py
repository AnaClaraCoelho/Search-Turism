# Generated by Django 4.0.8 on 2023-03-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_todo_city_todo_tourist_spot_todo_url_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='like',
            field=models.BooleanField(default=False),
        ),
    ]