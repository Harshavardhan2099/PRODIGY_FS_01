from django.urls import path
from secure import views

urlpatterns = [
    path('', views.home),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('admin-only/', views.admin_only_view, name='admin_only'),
]
