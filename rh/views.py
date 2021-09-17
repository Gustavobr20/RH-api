from rest_framework import viewsets

from .models import Funcionario
from .serializers import FuncionarioSerializer


class FuncionariosViewSet(viewsets.ModelViewSet):
    """
    Gerenciamento de Funcionários
    """
    serializer_class = FuncionarioSerializer
    queryset = Funcionario.objects.all()


