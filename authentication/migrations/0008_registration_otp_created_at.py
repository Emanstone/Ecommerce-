# Generated by Django 5.0.3 on 2024-03-16 09:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0007_registration_business_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="registration",
            name="otp_created_at",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
