# Generated by Django 1.9.1 on 2016-01-28 18:40
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("race", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="map",
            name="map_types",
            field=models.ManyToManyField(related_name="map_types", to="race.MapType"),
        )
    ]