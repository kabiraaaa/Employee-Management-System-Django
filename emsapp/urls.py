from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('demo', views.demo, name='demo'),
    path('employees/<int:employee_id>/', views.employee_details, name='employee_details')
]