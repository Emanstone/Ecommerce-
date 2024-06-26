# Generated by Django 5.0.3 on 2024-05-02 17:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_vendor_image_alter_vendor_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_vendor': True, 'vendor_application_status': 'approved'}, on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to=settings.AUTH_USER_MODEL),
        ),
    ]
