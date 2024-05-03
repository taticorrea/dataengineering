from rest_framework import generics
from .models import Aluno, Curso
from .serializer import AlunoSerializer, CursoSerializer

class ListAluno(generics.ListCreateAPIView):
    
    queryset         = Aluno.objects.all()
    serializer_class = AlunoSerializer

class ListCurso(generics.ListCreateAPIView):
    
    queryset         = Curso.objects.all()
    serializer_class = CursoSerializer    

