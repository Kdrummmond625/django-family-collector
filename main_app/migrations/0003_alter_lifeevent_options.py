# Generated by Django 5.0.1 on 2024-02-06 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_lifeevent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lifeevent',
            options={'ordering': ['-event_date']},
        ),
    ]