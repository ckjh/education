# Generated by Django 2.1.5 on 2019-10-17 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('admin01', '0021_auto_20191017_1941'),
    ]

    operations = [
        migrations.AddField(
            model_name='sk',
            name='sk_price',
            field=models.DecimalField(decimal_places=2, default=999.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 14, 35, 21, 118919, tzinfo=utc), verbose_name='会员结束时间'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 14, 35, 21, 118919, tzinfo=utc), verbose_name='会员开始时间'),
        ),
        migrations.AlterField(
            model_name='member',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 14, 35, 21, 88104, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='member',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 14, 35, 21, 88104, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 14, 35, 21, 120920, tzinfo=utc), verbose_name='优惠券结束时间'),
        ),
        migrations.AlterField(
            model_name='usercoupon',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 17, 14, 35, 21, 120920, tzinfo=utc), verbose_name='优惠券开始时间'),
        ),
    ]
