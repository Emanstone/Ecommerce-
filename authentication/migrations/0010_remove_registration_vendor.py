# Generated by Django 5.0.3 on 2024-05-02 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_registration_vendor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='vendor',
        ),
    ]