# Generated by Django 2.1.5 on 2019-10-08 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0005_auto_20191008_1206'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='stage',
            new_name='pathstage',
        ),
    ]
