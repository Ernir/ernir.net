# Generated by Django 3.0.6 on 2020-06-14 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("asylum", "0007_auto_20200607_1223"),
    ]

    operations = [
        migrations.AddField(
            model_name="agegendergroup",
            name="updated_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
