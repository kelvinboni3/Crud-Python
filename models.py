from django.db import models

# Create your models here.
class Regiao_Fruta(models.Model):
    Nome_Fruta = models.CharField(max_length=150)
    Nome_Regiao = models.CharField(max_length=150)


