# Generated by Django 3.2.12 on 2022-04-22 09:10
from django.db import migrations


def reset_team_timezone_to_UTC(apps, _) -> None:
    Team = apps.get_model("posthog", "Team")
    Team.objects.exclude(timezone="UTC").update(timezone="UTC")


class Migration(migrations.Migration):

    dependencies = [
        ("posthog", "0236_add_instance_setting_model"),
    ]

    def reverse(apps, _) -> None:
        pass

    operations = [
        migrations.RunPython(reset_team_timezone_to_UTC, reverse),
    ]