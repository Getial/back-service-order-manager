# Generated by Django 4.2.3 on 2023-11-04 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0025_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_necesary_spare_parts',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='spare_parts_list',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
