# Generated by Django 3.1.7 on 2021-03-30 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0002_auto_20210329_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='book_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='desc',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
