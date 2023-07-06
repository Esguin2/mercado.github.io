from django.urls import path
from .views import verCliente,InsertarCliente,PostyGet,Actualizar,frmodificar,Eliminar,LoginView, LogoutView, frmgestioncliente, PostyGet2, frmodificarpro, Actualizarpro, Eliminarpro, productoIns, verProd,frmodificarprod, Actualizarprod, Eliminarprod, ventaIns,ventaIns2,ventaver,CrearCuenta
from . import views

urlpatterns = [
    path('cliente',verCliente.as_view(), name='cliente'),
    path('insertar/',InsertarCliente.as_view(), name='insertar'),
    path('ambos/',PostyGet.as_view(), name='ambos'),
    path('actualizar/<str:cedula>/', views.frmodificar, name='actualizar'),
    path('actualizardat/<str:cedula>/',Actualizar.as_view(), name='actualizar2'),
    path('eliminar/<str:cedula>/', Eliminar.as_view(), name='eliminar'),
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('frmgestioncliente/', frmgestioncliente.as_view(), name='frmgestioncliente'),
    path('proveedor/',PostyGet2.as_view(), name='proveedor'),
    path('actualizarpro/<str:nit>/', views.frmodificarpro, name='actualizarpro'),
    path('actualizardatpro/<str:nit>/',Actualizarpro.as_view(), name='actualizar2pro'),
    path('eliminarpro/<str:nit>/', Eliminarpro.as_view(), name='eliminarpro'),
    path('insertarpro/',productoIns.as_view(), name='insertarpro'),
    path('verprod/',verProd.as_view(), name='verproductos'),
    path('actualizarprod/<str:codigo_producto>/', views.frmodificarprod, name='actualizarprod'),
    path('actualizardatprod/<str:codigo_producto>/',Actualizarprod.as_view(), name='actualizarprod2'),
    path('eliminarprod/<str:codigo_producto>/', Eliminarprod.as_view(), name='eliminarprod'),
    path('insertarventa/<str:codigo_producto>/',ventaIns.as_view(), name='ventainsertar'),
    path('insertarventa2/',ventaIns2.as_view(), name='ventainsertar2'),
    path('verventas/',ventaver.as_view(), name='verventas'),
    path('crearcuenta/',CrearCuenta.as_view(), name="crearcuenta")
]