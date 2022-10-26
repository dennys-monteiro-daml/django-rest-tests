from dataclasses import fields
from rest_framework import serializers

from projeto.project.escola.admin import Alunos
from .models import Aluno, LANGUAGE_CHOICES, LEXERS, STYLE_CHOICES

class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Alunos
    fields = '__all__'