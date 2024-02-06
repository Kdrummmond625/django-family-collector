# Generated by Django 5.0.1 on 2024-02-06 18:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('contents', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LifeEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('B', 'Birth'), ('D', 'Death'), ('M', 'Marriage'), ('G', 'Graduation'), ('M', 'Military Service'), ('R', 'Relocation'), ('O', 'Other')], default='B', max_length=1)),
                ('event_date', models.DateField()),
                ('event_description', models.TextField(blank=True)),
                ('family_member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.familymember')),
            ],
            options={
                'ordering': ['-event_date'],
            },
        ),
    ]
