# Generated by Django 4.2.3 on 2023-09-22 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0022_alter_user_options_rename_name_user_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='state',
            field=models.CharField(choices=[('received', 'Recibido'), ('admitted', 'Ingresado'), ('in_revision', 'En revision'), ('revised', 'Revisado'), ('waiting_for_spare_parts', 'En espera de repuestos'), ('in_repair', 'En reparacion'), ('repaired', 'Listo para entregar'), ('delivered', 'Entregado')], default=('received', 'Recibido'), max_length=25),
        ),
    ]
