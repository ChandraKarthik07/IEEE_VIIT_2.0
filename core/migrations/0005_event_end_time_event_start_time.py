# Generated by Django 4.2 on 2023-10-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_rename_date_event_end_date_event_mode_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="end_time",
            field=models.TimeField(default="00:00:00"),
        ),
        migrations.AddField(
            model_name="event",
            name="start_time",
            field=models.TimeField(default="00:00:00"),
        ),
    ]
