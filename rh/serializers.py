from rest_framework import serializers

from .models import Departamento, Funcionario


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Funcionario
        fields = ['id', 'nome', 'idade', 'telefone', 'departamento', 'cargo', 'salario', 'data_inicio']
