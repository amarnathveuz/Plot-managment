# Generated by Django 4.1.2 on 2022-11-04 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('super_admin', '0022_user_request_plot_reset_to_availale'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateField(auto_now=True)),
                ('tm', models.TimeField(auto_now=True)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=255, null=True)),
                ('d_text', models.TextField(null=True)),
                ('status_content', models.TextField(null=True)),
                ('action_appy_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_log_user_login_id', to='super_admin.user_details')),
                ('action_auth_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_log_auth_login_id', to=settings.AUTH_USER_MODEL)),
                ('user_mapping_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_log_login_id', to='super_admin.user_details')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]