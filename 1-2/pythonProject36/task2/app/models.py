from django.db import models


class Cat(models.Model):
    cat_name = models.CharField(max_length=20, default="")
    cat_breed = models.CharField(max_length=20, default="")


