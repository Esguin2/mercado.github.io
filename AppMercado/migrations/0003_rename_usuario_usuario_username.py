# Generated by Django 4.2.1 on 2023-06-27 01:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppMercado', '0002_usuario_alter_cliente_cedula'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='username',
        ),
    ]
