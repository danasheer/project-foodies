# Generated by Django 4.1.7 on 2023-03-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reciepes", "0002_remove_category_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="ingredient",
            name="reciepe",
        ),
        migrations.AddField(
            model_name="reciepe",
            name="ingredients",
            field=models.ManyToManyField(
                related_name="reciepies", to="reciepes.ingredient"
            ),
        ),
    ]
