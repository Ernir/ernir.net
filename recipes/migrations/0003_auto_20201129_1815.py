# Generated by Django 3.0.7 on 2020-11-29 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("recipes", "0002_auto_20201129_1758"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipeingredient",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ingredients",
                to="recipes.Recipe",
            ),
        ),
    ]