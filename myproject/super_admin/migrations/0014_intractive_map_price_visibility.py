# Generated by Django 4.1.2 on 2022-11-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0013_intractive_map_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='intractive_map',
            name='price_visibility',
            field=models.IntegerField(default=1, null=True),
        ),
    ]
