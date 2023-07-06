from typing import Any
from django.http.request import HttpRequest
from django.http.response import HttpResponseBase
from django.shortcuts import render, redirect
from django import http
from .models import Cliente, Usuario, Proveedor, Productos, Ventas
from django.views.generic import ListView,View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.



class verCliente(View):
    def get(self,request):
        datos=Cliente.objects.all().values()
        datoscli=list(datos)
        #return JsonResponse(datoscli, safe=False)
        return render(request,'consultacliente.html',{'datos':datoscli})

class InsertarCliente(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
        return render(request, 'clientes.html')

    def post(self,request):
        #datos=json.loads(request.body)
        
        cedula=request.POST.get('cedula')
        nombreCompleto=request.POST.get('nombreCompleto')
        dirrecion=request.POST.get('dirrecion')
        telefono=request.POST.get('telefono')
        correo=request.POST.get('correo')
        
        Cliente.objects.create(cedula=cedula,nombreCompleto=nombreCompleto,dirrecion=dirrecion,telefono=telefono,correo=correo)
        #return JsonResponse({'mensaje':'Datos guardados'})
        return redirect('cliente')

class PostyGet(View):  
    def get(self, request):
        datos=Cliente.objects.all().values()
        datoscli=list(datos)
        return render(request, 'clientes.html',{'datos':datoscli})
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        #datos=json.loads(request.body)
        
        cedula=request.POST.get('cedula')
        nombreCompleto=request.POST.get('nombreCompleto')
        dirrecion=request.POST.get('dirrecion')
        telefono=request.POST.get('telefono')
        correo=request.POST.get('correo')
        
        Cliente.objects.create(cedula=cedula,nombreCompleto=nombreCompleto,dirrecion=dirrecion,telefono=telefono,correo=correo)
        #return JsonResponse({'mensaje':'Datos guardados'})
        return redirect('ambos')
    
class Actualizar(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, cedula):
        try:
            registro = Cliente.objects.get(cedula=cedula)
        except Cliente.DoesNotExist:
            return JsonResponse({"error":"EL registro no existe"})
        
        registro.nombreCompleto = request.POST.get('nombreCompleto')
        registro.dirrecion = request.POST.get('dirrecion')
        registro.telefono = request.POST.get('telefono')
        registro.correo = request.POST.get('correo')
        registro.save()

        return redirect('ambos')

def frmodificar(request, cedula):
    cl = Cliente.objects.get(cedula = cedula)
    datos = {
        'cliente': cl
    }
    return render(request, 'actualizar.html', datos)

class Eliminar(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        return super().dispatch(request, *args, **kwargs)
    def get (self, request, cedula):
        try:
            resgitro=Cliente.objects.get(cedula=cedula)
        except Cliente.DoesNotExist:
            return JsonResponse({'error':'El registro no existe'})
        
        resgitro.delete()

        return redirect('ambos')
    
class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        if request.session.get('documento'):
            return redirect ('frmgestioncliente')
        return render (request, self.template_name)
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = Usuario.objects.get(username=username)
            if user.password == password:
                request.session['documento'] = user.documento
                return redirect ('frmgestioncliente')
            else:
                error_message = 'Credenciales invalidas'
                return render (request, self.template_name, {'error_mesage':error_message})
        except Usuario.DoesNotExist:
            error_message = 'Credenciales invalidas, Intentelo de nuevo'
            return render (request, self.template_name, {'error_mesage':error_message})

class LogoutView(View):
    def get(self, request):
        if request.session.get('documento'):
            del request.session ['documento']
        return redirect('login')
    
class PrincipalView(View):
    def get(self, request):
        if not request.session.get('documento'):
            return redirect ('login')

class OtrasVistas(View):
    def get(self, request):
        if not request.session.get('documento'):
            return redirect('login')

def principal(request):
    return render(request,'index.html')

class frmgestioncliente(View):
    def get(self,request):
        datos=Productos.objects.all().values()
        datospro=list(datos)
        return render(request, 'frmgestioncliente.html',{'datos':datospro})

# Proveedores
class PostyGet2(View):  
    def get(self, request):
        datos=Proveedor.objects.all().values()
        datospro=list(datos)
        return render(request, 'proveedores.html',{'datos':datospro})
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        #datos=json.loads(request.body)
        
        nit=request.POST.get('nit')
        nombreProveedor=request.POST.get('nombreProveedor')
        direccion=request.POST.get('direccion')
        telefono=request.POST.get('telefono')
        ciudad=request.POST.get('ciudad')
        
        Proveedor.objects.create(nit=nit,nombreProveedor=nombreProveedor,direccion=direccion,telefono=telefono,ciudad=ciudad)
        #return JsonResponse({'mensaje':'Datos guardados'})
        return redirect('proveedor')
    
class Actualizarpro(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, nit):
        try:
            registro = Proveedor.objects.get(nit=nit)
        except Proveedor.DoesNotExist:
            return JsonResponse({"error":"EL registro no existe"})
        
        registro.nombreProveedor = request.POST.get('nombreProveedor')
        registro.direccion = request.POST.get('direccion')
        registro.telefono = request.POST.get('telefono')
        registro.ciudad = request.POST.get('ciudad')
        registro.save()

        return redirect('proveedor')

def frmodificarpro(request, nit):
    cl = Proveedor.objects.get(nit = nit)
    datos = {
        'proveedor': cl
    }
    return render(request, 'actualizarpro.html', datos)

class Eliminarpro(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        return super().dispatch(request, *args, **kwargs)
    def get (self, request, nit):
        try:
            resgitro=Proveedor.objects.get(nit=nit)
        except Proveedor.DoesNotExist:
            return JsonResponse({'error':'El registro no existe'})
        
        resgitro.delete()

        return redirect('proveedor')
    
#Productos
class productoIns(View):  
    def get(self, request):
        datos=Proveedor.objects.all().values()
        datospro=list(datos)
        return render(request, 'productos.html',{'datos':datospro})
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):

        
        codigo_producto=request.POST.get('codigo_producto')
        nombreProducto=request.POST.get('nombreProducto')
        nitProveedor=request.POST.get('nitProveedor')
        compra=request.POST.get('compra')
        iva=request.POST.get('iva')
        
        nitProveedor = Proveedor.objects.get(nit=nitProveedor)

        Productos.objects.create(codigo_producto=codigo_producto,nombreProducto=nombreProducto,nitProveedor=nitProveedor,compra=compra,iva=iva)
        return redirect('verproductos')
    
class verProd(View):  
    def get(self, request):
        datosprod=Productos.objects.all().values()
        datosprod=list(datosprod)
        return render(request, 'verproductos.html',{'datosprod':datosprod})



class Actualizarprod(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    def post(self, request, codigo_producto):
        try:
            registro = Productos.objects.get(codigo_producto=codigo_producto)
        except Productos.DoesNotExist:
            return JsonResponse({"error":"EL registro no existe"})
        
        registro.nombreProducto = request.POST.get('nombreProducto')
        registro.compra = request.POST.get('compra')
        registro.compra = request.POST.get('compra')
        registro.save()

        return redirect('verproductos')
    
def frmodificarprod(request, codigo_producto):
    cl = Productos.objects.get(codigo_producto = codigo_producto)
    datosprod = {
        'productos': cl
    }
    return render(request, 'modiproductos.html', datosprod)

class Eliminarprod(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        return super().dispatch(request, *args, **kwargs)
    def get (self, request, codigo_producto):
        try:
            resgitro=Productos.objects.get(codigo_producto=codigo_producto)
        except Proveedor.DoesNotExist:
            return JsonResponse({'error':'El registro no existe'})
        
        resgitro.delete()

        return redirect('verproductos')

#Venta
class ventaIns(View):  
    def get(self, request, codigo_producto):
        datos = Cliente.objects.all().values()
        datospro = list(datos)
        contexto = {
            'datos': datospro,
            'valor': codigo_producto
        }
        return render(request, 'ventaCon.html', contexto)

    
class ventaIns2(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        

        id_cliente = request.POST.get('id_cliente')
        id_producto = request.POST.get('id_producto')

        id_cliente = Cliente.objects.get(cedula=id_cliente)
        id_producto = Productos.objects.get(codigo_producto=id_producto)  

        Ventas.objects.create(id_cliente=id_cliente, id_producto=id_producto)
        return redirect('frmgestioncliente')   
    
class ventaver(View):  
    def get(self, request):
        datos = Ventas.objects.all().values()
        datos = list(datos)
        
        return render(request, 'ventas.html', {'datos': datos})

#crear cuenta

class CrearCuenta(View):
    def get(self, request):
        
        return render(request,'crearcuenta.html')
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: Any, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self,request):
        #datos=json.loads(request.body)
        
        documento=request.POST.get('documento')
        username=request.POST.get('username')
        password=request.POST.get('password')
        rol=request.POST.get('rol')
        
        Usuario.objects.create(documento=documento,username=username,password=password,rol=rol)
        #return JsonResponse({'mensaje':'Datos guardados'})
        return redirect('login')
    