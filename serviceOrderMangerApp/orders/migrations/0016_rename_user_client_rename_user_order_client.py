# Generated by Django 4.2.3 on 2023-08-28 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_alter_order_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Client',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='user',
            new_name='client',
        ),
    ]