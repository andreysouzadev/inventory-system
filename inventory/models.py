from django.db import models

# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome
    
class Dispositivo(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="dispositivos")

    def __str__(self):
        return self.nome
