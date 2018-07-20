# Generated by Django 1.11.14 on 2018-07-11 22:23
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("accounts", "0002_auto_20160126_2355")]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="gender",
            field=models.IntegerField(
                blank=True,
                choices=[(1, "Unknown"), (2, "Male"), (3, "Female")],
                default=1,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="skin_body_color_raw",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="skin_feet_color_raw",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
