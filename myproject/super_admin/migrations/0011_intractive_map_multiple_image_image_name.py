# Generated by Django 4.1.2 on 2022-11-01 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0010_intractive_map_multiple_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='intractive_map_multiple_image',
            name='image_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
