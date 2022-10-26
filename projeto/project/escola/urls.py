from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from escola import views

urlpatterns = [
    path('aluno/', views.AlunoList.as_view()),
    path('aluno/<int:pk>/', views.AlunoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)