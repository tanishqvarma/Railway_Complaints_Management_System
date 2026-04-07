from django.urls import path
from . import views

urlpatterns = [
    path('accounts/profile/', views.user_dashboard, name='user_dashboard'),
    path('register/', views.register, name='register'),
    path('add/', views.add_complaint, name='add_complaint'),
    path('my/', views.my_complaints, name='my_complaints'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
]
