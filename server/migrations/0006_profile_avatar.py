# Generated by Django 2.0.2 on 2018-04-21 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_auto_20180421_0542'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.FileField(default=2, upload_to='uploads/'),
            preserve_default=False,
        ),
    ]
