# Generated by Django 4.2.6 on 2023-10-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yellow', '0002_category_alter_yellowm_business_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yellowm',
            name='business_category',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]
