# Generated by Django 5.0.1 on 2024-02-08 16:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_parentchild_child_alter_parentchild_parent'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymember',
            name='parents',
        ),
        migrations.AddField(
            model_name='familymember',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='lifeevent',
            name='event_type',
            field=models.CharField(choices=[('B', 'Birth'), ('D', 'Death'), ('M', 'Marriage'), ('G', 'Graduation'), ('S', 'Military Service'), ('R', 'Relocation'), ('O', 'Other')], default='B', max_length=1),
        ),
        migrations.DeleteModel(
            name='ParentChild',
        ),
    ]
