# Generated by Django 5.0.1 on 2024-02-06 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_parentchild_familymember_parents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parentchild',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_relation', to='main_app.familymember'),
        ),
        migrations.AlterField(
            model_name='parentchild',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_relation', to='main_app.familymember'),
        ),
    ]
