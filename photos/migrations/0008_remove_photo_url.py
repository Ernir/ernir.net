# Generated by Django 3.0.6 on 2020-06-01 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0007_auto_20200531_1201"),
    ]

    operations = [
        migrations.RemoveField(model_name="photo", name="url",),
    ]
