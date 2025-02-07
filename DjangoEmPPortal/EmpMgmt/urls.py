from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addEmp, name='addEmp'),
    path('empList/', views.getAllEmp, name='empList'),
    path('<int:empId>/', views.getEmpById, name='getEmpById'),
]