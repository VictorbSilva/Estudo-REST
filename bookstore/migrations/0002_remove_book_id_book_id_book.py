# Generated by Django 5.1.6 on 2025-02-27 14:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='id',
        ),
        migrations.AddField(
            model_name='book',
            name='id_book',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, null=True),
        ),
    ]
