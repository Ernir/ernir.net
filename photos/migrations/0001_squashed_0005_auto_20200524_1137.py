# Generated by Django 3.0.6 on 2020-05-24 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("photos", "0001_initial"),
        ("photos", "0002_auto_20200524_1112"),
        ("photos", "0003_photo_url"),
        ("photos", "0004_auto_20200524_1126"),
        ("photos", "0005_auto_20200524_1137"),
    ]

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gallery",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        height_field="height", upload_to="", width_field="width"
                    ),
                ),
                ("description", models.TextField()),
                (
                    "gallery",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="photos.Gallery"
                    ),
                ),
                ("height", models.IntegerField(default=1)),
                ("width", models.IntegerField(default=1)),
                ("url", models.URLField(max_length=1024, null=True)),
            ],
        ),
    ]
