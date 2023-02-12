# Generated by Django 4.0.5 on 2022-12-15 05:16

from django.db import migrations


def transfer_events(apps, schema_editor):
    UsageEvent = apps.get_model("metering_billing", "UsageEvent")
    Event = apps.get_model("metering_billing", "Event")
    for event in Event.objects.all():
        UsageEvent.objects.create(
            event_name=event.event_name,
            time_created=event.time_created,
            properties=event.properties,
            idempotency_id=event.idempotency_id,
            customer_id=event.customer_id,
            organization_id=event.organization_id,
            cust_id=event.cust_id,
            inserted_at=event.inserted_at,
        )


class Migration(migrations.Migration):
    dependencies = [
        (
            "metering_billing",
            "0121_usageevent_usageevent_metering_bi_organiz_c0b441_idx_and_more",
        ),
    ]

    operations = [
        migrations.RunPython(transfer_events, reverse_code=migrations.RunPython.noop),
    ]