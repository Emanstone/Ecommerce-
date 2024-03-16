# Generated by Django 5.0.3 on 2024-03-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='registration',
            name='is_emailverified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='is_vendor',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='registration',
            name='otp',
            field=models.CharField(default=234, max_length=6),
            preserve_default=False,
        ),
    ]
