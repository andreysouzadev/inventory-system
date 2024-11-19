from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_completo = models.CharField(max_length=100, default="Nome não informado")
    telefone = models.CharField(max_length=15)
    funcao = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username