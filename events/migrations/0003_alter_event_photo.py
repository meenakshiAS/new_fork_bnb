# Generated by Django 5.0.9 on 2024-10-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0002_alter_event_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="photo",
            field=models.ImageField(blank=True, null=True, upload_to="images"),
        ),
    ]
