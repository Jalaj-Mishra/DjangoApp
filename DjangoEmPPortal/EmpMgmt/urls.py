from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/login/', views.login_view, name='login'),
    path('api/add/', views.addEmp, name='addEmp'),
    path('empList/', views.getAllEmp, name='empList'),
    path('get/', views.getEmpById, name='getEmpById'),   # here we are passing id in query_params
    path('api/edit/<int:id>/', views.updateEmpById, name='updateEmp'),  # here we are passing the id in the url
    path('api/remove/<int:id>/', views.deleteEmp, name='deleteEmp'),  # here we are passing the id in the url
]