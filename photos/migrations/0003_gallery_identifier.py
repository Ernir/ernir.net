# Generated by Django 3.0.6 on 2020-05-24 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0002_auto_20200524_1208"),
    ]

    operations = [
        migrations.AddField(
            model_name="gallery",
            name="identifier",
            field=models.CharField(default=1, max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
