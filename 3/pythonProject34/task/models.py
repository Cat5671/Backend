from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name