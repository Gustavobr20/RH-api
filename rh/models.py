from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField(default=0)
    telefone = models.CharField(max_length=14)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    cargo = models.CharField(max_length=30)
    salario = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    data_inicio = models.DateField()

    def __str__(self):
        return self.nome
