from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class Aluno(models.Model):
  nome = models.CharField(max_length = 10)
  sobrenome = models.CharField(max_length = 20)
  cpf = models.CharField(max_length = 9)
  idade = models.DecimalField(max_digits = 2, decimal_places = 0)
  matricula_ativa = models.BooleanField(default=False)
  opcional = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
  style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

  class Meta:
        ordering = ['nome']

  def __str__(self):
      return self.nome
  