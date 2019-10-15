# Generated by Django 2.1.5 on 2019-10-15 00:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0013_auto_20191014_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('update_time', models.DateField(auto_now=True)),
                ('ratio', models.IntegerField()),
            ],
            options={
                'db_table': 'rule',
            },
        ),
        migrations.AlterField(
            model_name='coupon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 0, 35, 0, 699903, tzinfo=utc), verbose_name='会员结束时间'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 0, 35, 0, 698904, tzinfo=utc), verbose_name='会员开始时间'),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 0, 35, 0, 700903, tzinfo=utc), verbose_name='优惠券结束时间'),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 0, 35, 0, 699903, tzinfo=utc), verbose_name='优惠券开始时间'),
        ),
    ]
