# Generated by Django 3.0.6 on 2020-05-24 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0001_squashed_0005_auto_20200524_1137"),
    ]

    operations = [
        migrations.AlterField(
            model_name="photo", name="height", field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="photo", name="width", field=models.IntegerField(),
        ),
    ]
