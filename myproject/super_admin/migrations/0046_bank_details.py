# Generated by Django 4.1.2 on 2022-11-10 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('super_admin', '0045_customer_details_city_customer_details_company_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=255, null=True)),
                ('bank_identifier_code', models.CharField(max_length=255, null=True)),
                ('branch', models.CharField(max_length=255, null=True)),
                ('swift_code', models.CharField(max_length=255, null=True)),
                ('address', models.CharField(max_length=500, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(max_length=255, null=True)),
                ('dt', models.DateField(auto_now_add=True)),
                ('tm', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
