# Generated by Django 3.0.6 on 2020-05-31 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0006_auto_20200531_1148"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="gallery",
            options={
                "ordering": ("-start_date", "identifier"),
                "verbose_name_plural": "Galleries",
            },
        ),
    ]
