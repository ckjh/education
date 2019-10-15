# Generated by Django 2.1.5 on 2019-10-15 11:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0014_auto_20191015_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 11, 14, 14, 756362, tzinfo=utc), verbose_name='会员结束时间'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 11, 14, 14, 756362, tzinfo=utc), verbose_name='会员开始时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 11, 14, 14, 726359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 11, 14, 14, 726359, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 11, 14, 14, 757361, tzinfo=utc), verbose_name='优惠券结束时间'),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 15, 11, 14, 14, 757361, tzinfo=utc), verbose_name='优惠券开始时间'),
        ),
    ]
