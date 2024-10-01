# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('customize/<int:laptop_id>/', views.customize, name='customize'),
    path('customize/<int:laptop_id>/', views.customize, name='customize'),
    path('login/', views.login, name='login'),
    path('purchase/', views.purchase, name='purchase'),
    path('purchase_confirmation/', views.purchase_confirmation, name='purchase_confirmation'),
    path('review/', views.review, name='review'),
    # path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('confirmation/', views.purchase_confirmation, name='confirmation'),




    
]
  