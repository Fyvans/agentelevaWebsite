from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Servicos(models.Model):
    servicos1 = models.CharField(max_length=100)
    servicos2 = models.CharField(max_length=100)
    servicos3 = models.CharField(max_length=100)



    def __str__(self):
        return self.servicos1

    
class Contato(models.Model):
    hq = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)


    def __str__(self):
        return self.instagram
