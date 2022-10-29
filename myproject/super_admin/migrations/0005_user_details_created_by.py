# Generated by Django 4.1.2 on 2022-10-29 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('super_admin', '0004_user_details_atatchment'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_details',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_by_user_id', to=settings.AUTH_USER_MODEL),
        ),
    ]
