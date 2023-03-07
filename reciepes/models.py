from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=50)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='categories')

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return self.name


class Reciepe(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='reciepe/')
    description = models.TextField()
    steps = models.TextField()
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reciepies')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='reciepies')
    ingredients = models.ManyToManyField(
        Ingredient, related_name='reciepies')

    # def __str__(self):
    #     return self.title
