# Generated by Django 4.2.3 on 2023-08-12 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_alter_user_address_alter_user_second_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reason_for_damage',
            field=models.CharField(max_length=200, null=True),
        ),
    ]