from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^alunos/$', views.ListAluno.as_view(), name = 'list-alunos'),
    url(r'^cursos/$', views.ListCurso.as_view(), name = 'list-cursos'),

]
