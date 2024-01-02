from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):

    template_name = "home.html"


def criarQuiz(request):

    return render(request, 'criar-quiz.html')

def pesquisarQuiz(request):

    return render(request, 'pesquisar-quiz.html')

def login(request):

    return render(request, 'login.html')


