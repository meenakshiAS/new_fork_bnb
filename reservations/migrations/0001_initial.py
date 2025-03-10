# Generated by Django 5.0.9 on 2024-10-01 22:17

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("events", "0001_initial"),
        ("rooms", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Reservation",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("number_of_adults", models.IntegerField()),
                ("number_of_children", models.IntegerField()),
                ("check_in_date", models.DateField()),
                ("check_out_date", models.DateField()),
                ("total_cost", models.FloatField()),
                ("is_paid", models.BooleanField(default=False)),
                ("checked_in", models.BooleanField(default=False)),
                ("checked_out", models.BooleanField(default=False)),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_updated", models.DateTimeField(auto_now=True)),
                (
                    "events",
                    models.ManyToManyField(
                        related_name="events_reserved", to="events.event"
                    ),
                ),
                (
                    "rooms",
                    models.ManyToManyField(
                        related_name="rooms_reserved", to="rooms.room"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Guest",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("full_name", models.CharField(max_length=100)),
                ("is_adult", models.BooleanField(default=True)),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reservation_guests",
                        to="reservations.reservation",
                    ),
                ),
            ],
            options={
                "managed": True,
            },
        ),
    ]
