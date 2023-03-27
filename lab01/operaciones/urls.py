from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suma/<int:sum_n1>/<int:sum_n2>/', views.sumar, name='suma'),
    path('resta/<int:res_n1>/<int:res_n2>/', views.resta, name='resta'),
    path('multiplicacion/<int:pro_n1>/<int:pro_n2>/', views.multiplicacion, name='multiplicacion'),
]
