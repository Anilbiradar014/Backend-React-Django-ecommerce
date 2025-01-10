from django.urls import path
from . import views

urlpatterns = [
    path('',views.getRoutes, name="List all routes"),
    path('products/',views.getProducts, name="List all routes"),
    path('products/<str:pk>/',views.getProductByID, name="Get product based on ID"),
]
