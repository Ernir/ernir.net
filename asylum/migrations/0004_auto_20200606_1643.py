# Generated by Django 3.0.6 on 2020-06-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("asylum", "0003_auto_20200606_1445"),
    ]

    operations = [
        migrations.AlterField(
            model_name="agegendergroup",
            name="boys",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="agegendergroup",
            name="girls",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="agegendergroup",
            name="men",
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="agegendergroup",
            name="women",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
