# Generated by Django 2.0.9 on 2018-11-22 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180711_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Unknown'), (2, 'Male'), (3, 'Female')], default=1),
        ),
    ]