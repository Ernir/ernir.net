# Generated by Django 3.0.6 on 2020-06-06 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("asylum", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="year", options={"ordering": ("starting_date",)},
        ),
    ]