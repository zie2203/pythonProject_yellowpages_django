# Generated by Django 4.2.6 on 2023-10-17 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yellow', '0005_reviews'),
    ]

    operations = [
        migrations.AddField(
            model_name='yellowm',
            name='is_enable',
            field=models.BooleanField(default=False),
        ),
    ]
