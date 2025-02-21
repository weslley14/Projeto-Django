from django.db import models

class Produto(models.Model):
    id_produto = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=200)
    serie = models.TextField(max_length=200)
    quantidade = models.IntegerField()