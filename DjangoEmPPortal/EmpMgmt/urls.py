from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addEmp, name='addEmp'),
    path('empList/', views.getAllEmp, name='empList'),
    path('get/', views.getEmpById, name='getEmpById'),   # here we are passing id in query_params
    path('edit/<int:id>', views.updateEmpById, name='updateEmp'),  # here we are passing the id in the url
    path('remove/<int:id>', views.deleteEmp, name='deleteEmp'),  # here we are passing the id in the url
]