# Generated by Django 2.1.5 on 2019-10-07 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0003_usercoupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathstage',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='course',
            name='info',
            field=models.CharField(max_length=255, verbose_name='课程简介'),
        ),
    ]
