# Generated by Django 4.1.2 on 2022-11-04 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0021_alter_user_access_property_mapping_mapping_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request_plot',
            name='reset_to_availale',
            field=models.IntegerField(null=True),
        ),
    ]
