# Generated by Django 2.1.5 on 2019-10-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0006_auto_20191008_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='video',
            field=models.CharField(max_length=255, verbose_name='视频连接'),
        ),
    ]