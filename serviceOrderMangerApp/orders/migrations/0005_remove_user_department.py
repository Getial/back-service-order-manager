# Generated by Django 4.2.3 on 2023-08-05 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_brand_options_alter_reference_exploded_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='department',
        ),
    ]
