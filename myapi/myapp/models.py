from django.db import models

class Aluno(models.Model):

    class Meta:
        db_table = 'aluno-db'

    nome       = models.CharField(max_length=200)
    cpf        = models.CharField(max_length=200)
    matricula  = models.CharField(max_length=200)
    idade      = models.IntegerField()


class Curso(models.Model):

    class Meta:
        db_table = 'curso-db'

    nome      = models.CharField(max_length=200)
    credito   = models.IntegerField() 
    professor = models.CharField(max_length=200)
