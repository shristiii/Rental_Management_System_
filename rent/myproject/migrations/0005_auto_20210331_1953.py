# Generated by Django 3.1.7 on 2021-03-31 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0004_booking_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='desc',
        ),
        migrations.AddField(
            model_name='info',
            name='hotel_Main_Img',
            field=models.ImageField(default=123, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='price',
            field=models.CharField(default='123', max_length=200, null=True),
        ),
    ]