# Generated by Django 4.1.2 on 2022-11-08 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0027_alter_intractive_map_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intractive_map',
            name='Price',
            field=models.FloatField(max_length=255, null=True),
        ),
    ]
