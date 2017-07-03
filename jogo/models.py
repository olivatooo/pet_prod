from django.db import models
from django.core.validators import MinValueValidator
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator


# Tabela Médico
class Medico(models.Model):
    classificacao = ((1,'1'),(2,'2'),(3,'3'))
    # id = models.AutoField(u'id', primary_key=True, unique=True)
    # Só deixei comentado aqui para lembrar todos de fazer isso!
    perfil = models.IntegerField(validators=[MinValueValidator(1)])
    salario = models.FloatField(validators=[MinValueValidator(0.0)])
    expertise = models.IntegerField(default=1, choices=classificacao)
    atendimento = models.IntegerField(default=1, choices=classificacao)
    pontualidade = models.IntegerField(default=1, choices=classificacao)
    # Não esqueçam de fazer a migração para o novo BD:
    # Tools -> Run manage.py task -> makemigrations -> migrate


class Evento(models.Model):
    class Meta:
        verbose_name = 'evento'
        verbose_name_plural = 'eventos'

    nome = models.CharField(max_length=50)
    multiplicador_classeA = models.FloatField(validators=[MinValueValidator(0.0)])
    multiplicador_classeB = models.FloatField(validators=[MinValueValidator(0.0)])
    multiplicador_classeC = models.FloatField(validators=[MinValueValidator(0.0)])
    multiplicador_classeD = models.FloatField(validators=[MinValueValidator(0.0)])
    multiplicador_classeE = models.FloatField(validators=[MinValueValidator(0.0)])



class Emprestimo(models.Model):
    valor = models.FloatField(validators=[MinValueValidator(1.0)])
#Tabela Time
class Time(models.Model):
    nome = models.CharField(max_length=20) #NOME DO TIME
    login = models.CharField(max_length=15) #LOGIN PARA ENTRAR NO SISTEMA
    senha = models.CharField(max_length=20)
    caixa = models.FloatField(validators=[MinValueValidator(0.0)]) #QUANTIDADE NO CAIXA


class Classe_Social(models.Model):
    classificacao = ((1, '1'), (2, '2'), (3, '3'))
    #id = models.AutoField(u'id', primary_key=True, unique=True)
    nome = models.CharField(max_length=200)
    preco_atendimento = models.FloatField(validators=[MinValueValidator(0.0)])
    nivel_especialidade = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    nivel_tecnologia = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    media_conforto = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
    velocidade_atendimento = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(3.0)])
class Rodada(models.Model):
    verbose_name = 'rodada'
    verbose_name_plural = 'rodadas'

    numeroRodada = models.IntegerField(validators=[MinValueValidator(1)])
    duracao = models.IntegerField(validators=[MinValueValidator(1)])
    # TODO implementar apos a implementacao da classe evento
    # evento = models.ForeignKey(Evento, on_delete=models.CASCADE, default=1)
