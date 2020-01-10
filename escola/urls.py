"""escola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alunos.views import *

urlpatterns = [
    path('deletar/aluno/<int:id>', deletar_aluno),
    path('atualizar/aluno/<int:id>', atualizar_aluno),
    path('aluno/<int:id>', detalhes_aluno),
    path('lista/alunos/', lista_alunos),
    path('cadastrar/alunos/', cadastrar_aluno),
    path('', home),
    path('admin/', admin.site.urls),
]
