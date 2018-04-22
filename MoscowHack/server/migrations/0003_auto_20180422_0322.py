# Generated by Django 2.0.2 on 2018-04-22 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20180421_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hackratebyuser',
            name='rate',
            field=models.IntegerField(choices=[(1, 'Very bad'), (2, 'Bad'), (3, 'Medium'), (4, 'Good'), (5, 'Perfect')], validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
