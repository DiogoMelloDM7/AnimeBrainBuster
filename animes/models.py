from django.db import models

# Create your models here.

class Quiz(models.Model):

    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Pergunta(models.Model):

    pergunta = models.CharField(max_length=200)
    respostaA = models.CharField(max_length=200)
    respostaB = models.CharField(max_length=200)
    respostaC = models.CharField(max_length=200)
    respostaD = models.CharField(max_length=200)
    respostaCorreta = models.CharField(max_length=200)
    quiz = models.ForeignKey("Quiz", related_name="quiz", on_delete=models.CASCADE)

    def __str__(self):
        return f'Pergunta - {self.pk} - {self.quiz.nome}'
