from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('inicio/', views.inicio, name="inicio"),
	path('empresa/', views.empresa, name="empresa"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('faq/', views.faq, name="faq"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('index/', views.index, name="index"),
	path('listadoProducto/', views.listadoProducto, name="listado_producto"),
	path('detalleProducto/', views.detalleProducto, name="detalle_producto"),
]