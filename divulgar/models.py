from django.db import models
from django.contrib.auth.models import User
from divulgar.variaveis import *

class Raca(models.Model):
    raca = models.CharField(max_length=120)

    def __str__(self):
        return self.raca


class Pet(models.Model):
    especies_escolhas = [('C', 'Cachorro'), ('G', 'Gato')]

    tag_escolhas = [
            (docil, docil),(bravo, bravo),
            (carinhoso, carinhoso),(manso, manso),
            (protetor, protetor),(agitado, agitado),
            (vacinado, vacinado),(castrado, castrado),
            (pelagem_longa, pelagem_longa), (especial, especial),
            (resgatado, resgatado), (pelagem_curta, pelagem_curta),
            (adestrado, adestrado), (hipoalergico, hipoalergico),
            ]
    
    status_escolhas = [(adotado, adotado), (para_adocao, para_adocao)]

    especie = models.CharField(choices=especies_escolhas, max_length=1)
    raca = models.ForeignKey(Raca, on_delete=models.PROTECT)
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=120)
    descricao = models.TextField()
    cidade = models.CharField(max_length=120)
    telefone = models.CharField(max_length=14)
    status = models.CharField(choices=status_escolhas, max_length=20, default=para_adocao)
    tag1 = models.CharField(max_length=120, choices=tag_escolhas, blank=True)
    tag2 = models.CharField(max_length=120, choices=tag_escolhas, blank=True)
    tag3 = models.CharField(max_length=120, choices=tag_escolhas, blank=True)
    tag4 = models.CharField(max_length=120, choices=tag_escolhas, blank=True)
    foto = models.ImageField(upload_to='pets')


    def __str__(self):
        return self.nome


