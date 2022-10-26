from django.contrib import admin
from escola.models import Aluno
# Register your models here.

class Alunos(admin.ModelAdmin):
  list_display = ('nome','sobrenome', 'cpf', 'idade', 'matricula_ativa','opcional', 'style')
  list_display_links = ('nome','sobrenome', 'cpf', 'idade', 'matricula_ativa','opcional', 'style')
  search_fields = ('nome','sobrenome', 'cpf', 'idade', 'matricula_ativa','opcional', 'style')

admin.site.register(Aluno, Alunos)