# Generated by Django 4.2.3 on 2023-08-18 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_rename_reason_for_damage_order_reason_for_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='serial',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
