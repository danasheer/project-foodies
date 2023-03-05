from django.contrib import admin
from .models import Category, Reciepe, Ingredient

# Register your models here.

admin.site.register(Category)
admin.site.register(Reciepe)
admin.site.register(Ingredient)
