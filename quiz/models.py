from django.db import models


class QuestionsModel(models.Model):
    question = models.CharField(max_length=200, null=True, verbose_name='Pergunta')
    op1 = models.CharField(max_length=200, null=True, verbose_name='Opção 1')
    op2 = models.CharField(max_length=200, null=True, verbose_name='Opção 2')
    op3 = models.CharField(max_length=200, null=True, verbose_name='Opção 3')
    op4 = models.CharField(max_length=200, null=True, verbose_name='Opção 4')
    ans = models.CharField(max_length=200, null=True, verbose_name='Resposta (Ex: "option1")')
    q_number = models.BigIntegerField(unique=True, verbose_name='Questao Nº')
    mostrar = models.BooleanField(default=True)
