from django.db import models


class Buyer(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name
