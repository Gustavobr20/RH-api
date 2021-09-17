from django.contrib import admin

from .models import Departamento, Funcionario

admin.site.register([Departamento, Funcionario])
