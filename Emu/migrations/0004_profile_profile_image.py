# Generated by Django 4.2.3 on 2023-08-01 12:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Emu", "0003_tweet"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
