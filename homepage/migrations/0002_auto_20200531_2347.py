# Generated by Django 3.0.6 on 2020-05-31 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="frontpagesection", options={"ordering": ("the_order",)},
        ),
        migrations.AddField(
            model_name="frontpagesection",
            name="the_order",
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
        ),
    ]
