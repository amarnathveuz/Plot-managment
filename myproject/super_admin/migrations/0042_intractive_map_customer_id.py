# Generated by Django 4.1.2 on 2022-11-10 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0041_customer_details_user_request_plot_customer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='intractive_map',
            name='customer_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
