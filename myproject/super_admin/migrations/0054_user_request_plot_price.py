# Generated by Django 4.1.2 on 2022-11-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0053_alter_user_details_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_request_plot',
            name='Price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
