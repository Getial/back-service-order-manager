# Generated by Django 3.2.12 on 2024-01-13 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0029_auto_20240103_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='spare_parts_list',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
