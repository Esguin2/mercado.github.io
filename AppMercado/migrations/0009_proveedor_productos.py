# Generated by Django 4.2.1 on 2023-07-02 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppMercado', '0008_alter_cliente_cedula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('nit', models.TextField(max_length=20, primary_key=True, serialize=False)),
                ('nombreProveedor', models.TextField(max_length=30)),
                ('direccion', models.TextField(max_length=30)),
                ('telefono', models.TextField(max_length=30)),
                ('ciudad', models.TextField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('codigo_producto', models.TextField(max_length=30, primary_key=True, serialize=False)),
                ('nombreProducto', models.TextField(max_length=30)),
                ('compra', models.IntegerField()),
                ('iva', models.IntegerField()),
                ('nitProveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AppMercado.proveedor')),
            ],
        ),
    ]
