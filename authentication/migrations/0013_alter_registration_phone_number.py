# Generated by Django 5.0.3 on 2024-05-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_registration_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone_number',
            field=models.CharField(default=0, max_length=11),
        ),
    ]