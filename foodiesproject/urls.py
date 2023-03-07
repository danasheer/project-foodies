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
from reciepes.views import RecipieDetailView, RecipieUpdateView, RecipeDeleteView, listReciepeView, CreateReciepeView, CreateIngrediantView, listingrediantView, UpdateIngrediantView, DeleteIngrediantView, CreateCategoryView, listCategoryView, UpdateCategoryView, DeleteCategoryView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/register/", views.UserCreateView.as_view(), name="register"),
    path("api/login/", views.UserLoginAPIView.as_view(), name="login"),
    path("api/recipe/delete/<int:object_id>/",
         RecipeDeleteView.as_view(), name="delete_recipe"),
    path("api/recipe/update/<int:object_id>/",
         RecipieUpdateView.as_view(), name="update_recipe"),
    path("api/recipe/detail/<int:object_id>/",
         RecipieDetailView.as_view(), name="detail_recipe"),
    path("api/recipes/",
         listReciepeView.as_view(), name="list"),
    path("api/recipe/create/", CreateReciepeView.as_view(), name="create_recipe"),
    path("api/ingrediants/create/",
         CreateIngrediantView.as_view(), name="create_ingrediant"),
    path("api/ingrediants/", listingrediantView.as_view(), name="list_ingrediants"),
    path("api/ingrediants/update/<int:object_id>/",
         UpdateIngrediantView.as_view(), name="update_ingrediant"),
    path("api/ingrediants/delete/<int:object_id>/",
         DeleteIngrediantView.as_view(), name="delete_ingrediant"),
    path("api/category/create/", CreateCategoryView.as_view(),
         name="create_category"),
    path("api/category/", listCategoryView.as_view(), name="list_category"),
    path("api/category/update/<int:object_id>/",
         UpdateCategoryView.as_view(), name="update_category"),
    path("api/category/delete/<int:object_id>/",
         DeleteCategoryView.as_view(), name="delete_category"),
]
