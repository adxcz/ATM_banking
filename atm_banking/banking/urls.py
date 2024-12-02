from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('deposit/', views.deposit, name='deposit'),
    path('withdraw/', views.withdraw, name='withdraw'),
    path('sendmoney/', views.send_money, name='sendmoney'),  # Add this line
    path('change_pin/', views.change_pin, name='change_pin'),
    path('contact/', views.contact, name='contact'),
    path('', views.home, name='home'),
]