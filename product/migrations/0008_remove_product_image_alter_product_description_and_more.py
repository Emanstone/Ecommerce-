# Generated by Django 5.0.3 on 2024-05-03 08:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_product'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_details',
            field=models.TextField(verbose_name=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(limit_choices_to={'is_vendor': True, 'vendor_application_status': 'approved'}, on_delete=django.db.models.deletion.CASCADE, related_name='vendors', to=settings.AUTH_USER_MODEL),
        ),
    ]
