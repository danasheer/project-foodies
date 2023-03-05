from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name


class Reciepe(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='reciepe/')
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reciepe')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='reciepe')

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    reciepe = models.ForeignKey(
        Reciepe, on_delete=models.CASCADE, related_name='ingredient')

    def __str__(self):
        return self.name
