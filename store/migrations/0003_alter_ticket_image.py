# Generated by Django 3.2.5 on 2021-09-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_alter_ticket_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="D:\\src\\OCP09\\media"
            ),
        ),
    ]
