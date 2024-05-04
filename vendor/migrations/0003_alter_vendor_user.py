# Generated by Django 5.0.3 on 2024-05-03 10:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0002_alter_vendor_image_alter_vendor_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_vendor': True, 'vendor_application_status': 'approved', 'vendor_id': True}, on_delete=django.db.models.deletion.CASCADE, related_name='vendor', to=settings.AUTH_USER_MODEL),
        ),
    ]