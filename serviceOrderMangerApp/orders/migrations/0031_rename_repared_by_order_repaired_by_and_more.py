# Generated by Django 5.1.6 on 2025-03-01 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_alter_order_spare_parts_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='repared_by',
            new_name='repaired_by',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='checked_by',
            new_name='revised_by',
        ),
        migrations.AddField(
            model_name='order',
            name='warranty_denial_reason',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='admitted_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha ingresado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivered_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha entregado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quoted_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha cotizado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='reapired_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha reparado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='revised_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha revisado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='warranty_denial_date',
            field=models.DateTimeField(null=True, verbose_name='Fecha negacion garantia'),
        ),
    ]
