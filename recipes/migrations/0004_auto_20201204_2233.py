# Generated by Django 3.0.7 on 2020-12-04 22:33

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0003_auto_20201129_1815"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="recipe",
            managers=[("full_recipe", django.db.models.manager.Manager()),],
        ),
    ]
