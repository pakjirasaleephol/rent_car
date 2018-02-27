"""rent_car URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('login/', auth_views.LoginView.as_view()),
    path('home/', views.home, name='home'),
    # path('', views.CarListView.as_view(), name='carlist')
    # #path('login/', auth_views.login, {'template_name': 'core/login.html'}, name='login'),
    # #path('logout/', auth_views.logout, name='logout'),
    path('carlist/',views.CarListView.as_view(), name='car_list'),
    path('rentcar/', views.CreateRentView.as_view(), name='rent_car'),
    path('createperson/', views.CreatePersonView.as_view(), name='create_person'),
    path('rentlist/',views.RentListView.as_view(), name='rent_list'),
    path('personlist/',views.ListPersonView.as_view(), name='person_list'),
]
