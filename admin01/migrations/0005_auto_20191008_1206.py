# Generated by Django 2.1.5 on 2019-10-08 04:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0004_auto_20191008_0746'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='stage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin01.PathStage', verbose_name='阶段外键'),
        ),
        migrations.AlterField(
            model_name='course',
            name='path',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin01.Path', verbose_name='路径'),
        ),
    ]
