# Generated by Django 4.2.3 on 2023-08-28 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_rename_collaborator_user_alter_user_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='repared_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='reparado_por', to='orders.user'),
        ),
    ]
