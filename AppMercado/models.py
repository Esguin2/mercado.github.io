from django.db import models

# Create your models here.

class Usuario(models.Model):
    documento = models.TextField(max_length=20, primary_key=True)
    username = models.TextField(max_length=30, default='valor_predeterminado')
    password = models.CharField(max_length=255)
    rol = models.CharField(max_length=30)

class Cliente(models.Model):
    cedula=models.TextField(max_length=20,primary_key=True, )
    nombreCompleto=models.TextField(max_length=30)
    dirrecion=models.TextField(max_length=30)
    telefono=models.TextField(max_length=30)
    correo=models.TextField(max_length=30)

class Proveedor(models.Model):
    nit=models.TextField(max_length=20,primary_key=True, )
    nombreProveedor = models.TextField(max_length=30)
    direccion = models.TextField(max_length=30)
    telefono = models.TextField(max_length=30)
    ciudad = models.TextField(max_length=30)

class Productos(models.Model):
    codigo_producto = models.TextField(max_length=30, primary_key=True)
    nombreProducto = models.TextField(max_length=30)
    nitProveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    compra = models.IntegerField()
    iva = models.IntegerField()

class Ventas(models.Model):
    id_venta = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)


