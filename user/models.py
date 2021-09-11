from django.db import models

class Users(models.Model):
    email = models.EmailField(null=False, max_length=254, unique=True)
    password = models.CharField(null=False, max_length=64)
    username = models.CharField(null=False, unique=True, max_length=30)
    address = models.TextField(null=False, max_length=250)

    class Meta:
        db_table = "user"