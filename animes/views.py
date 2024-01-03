from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Quiz, Pergunta

lista_de_perguntas_do_quiz = []

def limpar_lista_de_perguntas_do_quiz():
    return []

class Home(TemplateView):

    template_name = "home.html"


def criarQuiz(request):

    if request.method == 'POST':
        button_type = request.POST.get("confirm")

        if button_type == 'criar-pergunta':
            pergunta = request.POST.get('pergunta')
            respostaA = request.POST.get('respostaA')
            respostaB = request.POST.get('respostaB')
            respostaC = request.POST.get('respostaC')
            respostaD = request.POST.get('respostaD')
            respostaCorreta = request.POST.get('resposta-correta')

            questoes = {}
            questoes['pergunta'] = pergunta
            questoes['respostaA'] = respostaA
            questoes['respostaB'] = respostaB
            questoes['respostaC'] = respostaC
            questoes['respostaD'] = respostaD
            questoes['respostaCorreta'] = respostaCorreta

            lista_de_perguntas_do_quiz.append(questoes)
            print(lista_de_perguntas_do_quiz)
        
        if button_type == 'finalizar-quiz':
            nome_quiz = request.POST.get('nome-quiz')
            quiz = Quiz.objects.create(nome = nome_quiz)
            for item in lista_de_perguntas_do_quiz:
                Pergunta.objects.create(
                    pergunta=item['pergunta'],
                    respostaA=item['respostaA'],
                    respostaB=item['respostaB'],
                    respostaC=item['respostaC'],
                    respostaD=item['respostaD'],
                    respostaCorreta=item['respostaCorreta'],
                    quiz=quiz)
            lista_de_perguntas_do_quiz = limpar_lista_de_perguntas_do_quiz()
                

    return render(request, 'criar-quiz.html')

def pesquisarQuiz(request):

    return render(request, 'pesquisar-quiz.html')

def login(request):

    return render(request, 'login.html')


