# Generated by Django 4.2.3 on 2023-08-06 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_remove_user_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='document',
            field=models.CharField(max_length=20, unique=True, verbose_name='Documento'),
        ),
    ]