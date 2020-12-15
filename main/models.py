from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100,blank=True)
    catchphrase = models.CharField(max_length=200,blank=True)

    def __str__(self):
        if self.email:
            return self.email
        else:
            return self.username
