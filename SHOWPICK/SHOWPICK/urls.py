"""SHOWPICK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from app import views

urlpatterns = [
    # social login
    path('accounts/', include('allauth.urls')),

    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('CEO_map', views.ceo_map, name = "CEO_map"),
    path('Customer_map', views.customer_map, name = "Customer_map"),
    path('testing_map', views.testing_map, name = "testing_map"),
    path('Customer_map_Anam', views.customer_map_Anam, name = "Customer_map_Anam"),
    path('Customer_map_Jongam', views.customer_map_Jongam, name = "Customer_map_Jongam"),

    path('mypage/', views.mypage, name="mypage")
    path('CEO_map_Anam', views.ceo_map_Anam, name = "CEO_map_Anam"),
    path('CEO_map_Jongam', views.ceo_map_Jongam, name = "CEO_map_Jongam"),
    path('vote/', views.home, name="vote"),
    path('mypage/', views.home, name="mypage"),

    path('vote/', views.vote_index, name="vote_index"),
    path('vote/<int:qid>', views.vote_category, name="vote_category"),
    path('vote_store/', views.vote_store, name="vote_store"),
    path('result/<int:q_id>/', views.vote_result, name="vote_result"),

]
