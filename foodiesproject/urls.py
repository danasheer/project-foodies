"""foodiesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls.conf import include
from rest_framework import routers
from accounts import views
from reciepes.views import RecipieDetailView, RecipieUpdateView, RecipeDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/", views.UserCreateView.as_view(), name="register"),
    path("api/login/", views.UserLoginAPIView.as_view(), name="login"),
    path("api/recipe/delete/<int:object_id>/",
         RecipeDeleteView.as_view(), name="delete"),
    path("api/recipe/update/<int:object_id>/",
         RecipieUpdateView.as_view(), name="update"),
    path("api/recipe/detail/<int:object_id>/",
         RecipieDetailView.as_view(), name="retreive"),
]
