# Generated by Django 2.1.5 on 2019-10-14 15:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0011_auto_20191014_2353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercoupon',
            name='code',
        ),
        migrations.AlterField(
            model_name='coupon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 15, 55, 14, 715250, tzinfo=utc), verbose_name='会员结束时间'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 15, 55, 14, 715250, tzinfo=utc), verbose_name='会员开始时间'),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 15, 55, 14, 716251, tzinfo=utc), verbose_name='优惠券结束时间'),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 14, 15, 55, 14, 716251, tzinfo=utc), verbose_name='优惠券开始时间'),
        ),
    ]
