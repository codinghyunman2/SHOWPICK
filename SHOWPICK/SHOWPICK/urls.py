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
    path('Shop_info_Anam', views.Shop_info_Anam, name = "Shop_info_Anam"),
    path('shop_info_jongam', views.shop_info_jongam, name = "shop_info_jongam"),
    path('mypage/', views.mypage, name="mypage"),

    path('CEO_map_Anam', views.ceo_map_Anam, name = "CEO_map_Anam"),
    path('CEO_map_Jongam', views.ceo_map_Jongam, name = "CEO_map_Jongam"),
 
    path('customer_title/<int:vote_pk>', views.customer_title, name = "customer_title"),
    path('customer_small_category/<int:vote_pk>', views.customer_small_category, name ="customer_small_category"),
    path('Show_CEO', views.show_ceo, name= "Show_CEO"),
    path('Vote_Ending', views.vote_ending, name = "Vote_Ending"),   

    path('Shop_info_Anam', views.shop_info_anam, name="Shop_info_Anam"),

]
