# Generated by Django 3.0.6 on 2020-05-31 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20200530_1557'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ('image',)},
        ),
    ]
