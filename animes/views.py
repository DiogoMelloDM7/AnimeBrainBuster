from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Quiz, Pergunta
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.urls import resolve

lista_de_perguntas_do_quiz = []

def limpar_lista_de_perguntas_do_quiz():
    return []

def verifica_url(request):
    current_url = request.path
    match = resolve(current_url)
    if not match.url_name == "criarquiz":
        global lista_de_perguntas_do_quiz
        lista_de_perguntas_do_quiz = limpar_lista_de_perguntas_do_quiz()

class Home(TemplateView):

    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        verifica_url(request)
        return render(request, self.template_name)



def criarQuiz(request):

    global lista_de_perguntas_do_quiz
    if request.user.is_authenticated:
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
                questoes['Pergunta'] = pergunta
                questoes['Resposta A'] = respostaA
                questoes['Resposta B'] = respostaB
                questoes['Resposta C'] = respostaC
                questoes['Resposta D'] = respostaD
                questoes['Resposta Correta'] = respostaCorreta

                lista_de_perguntas_do_quiz.append(questoes)
                print(lista_de_perguntas_do_quiz)
            
            if button_type == 'finalizar-quiz':
                if lista_de_perguntas_do_quiz:
                    nome_quiz = request.POST.get('nome-quiz')
                    usuario_criador = request.user
                    quiz = Quiz.objects.create(nome = nome_quiz, usuario=usuario_criador)
                    for item in lista_de_perguntas_do_quiz:
                        Pergunta.objects.create(
                            pergunta=item['Pergunta'],
                            respostaA=item['Resposta A'],
                            respostaB=item['Resposta B'],
                            respostaC=item['Resposta C'],
                            respostaD=item['Resposta D'],
                            respostaCorreta=item['Resposta Correta'],
                            quiz=quiz)
                    lista_de_perguntas_do_quiz = limpar_lista_de_perguntas_do_quiz()
                    messages.success(request, "Quiz criado com sucesso!")
                else: 
                    messages.error(request, "Para criar o quiz você deve inserir ao menos uma pergunta!")
            if button_type == "del":
                indice = request.POST.get("indice")
                try:
                    indice = int(indice)
                    indice -= 1
                except:
                    indice = None
                try:
                    if indice:
                        lista_de_perguntas_do_quiz.pop(indice)
                    else:
                        lista_de_perguntas_do_quiz.pop(0)
                    return render(request, 'criar-quiz.html', {'perguntas_do_quiz': lista_de_perguntas_do_quiz})
                except:
                    return render(request, 'criar-quiz.html', {'perguntas_do_quiz': lista_de_perguntas_do_quiz})


        return render(request, 'criar-quiz.html', {'perguntas_do_quiz': lista_de_perguntas_do_quiz})
    else:
        return redirect('animes:login')

class PesquisarQuiz(LoginRequiredMixin, ListView):
    template_name = 'pesquisar-quiz.html'
    model = Quiz

    def post(self, request, *args, **kwargs):
        verifica_url(request)
        nome_quiz = request.POST.get('nome_pesquisa_quiz')
        lista_quiz = Quiz.objects.filter(nome__icontains=nome_quiz)
    
        return render(request, self.template_name, {"object_list": lista_quiz})


class QuizIndividual(LoginRequiredMixin, ListView):
    template_name = "quiz-individual.html"
    model = Pergunta
    context_object_name = 'object_list'


    def get_queryset(self):
        ID_quiz_url = self.kwargs.get('pk')
        perguntas = Pergunta.objects.filter(quiz__pk=ID_quiz_url)
        return perguntas

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ID_quiz_url = self.kwargs.get('pk')
        nome_quiz = get_object_or_404(Quiz, pk=ID_quiz_url)
        context['quiz'] = nome_quiz.nome
        return context

    def post(self, request, *args, **kwargs):
        verifica_url(request)
        quant_perguntas = int(request.POST.get('quant_perguntas', 0)) + 1
        respostas_usuario = []
        respostas_corretas = []
        for indice in range(quant_perguntas):
            resposta = request.POST.get(f'resposta-questao-{indice}')
            if resposta is not None:
                respostas_usuario.append(resposta)
        perguntas = self.get_queryset()
        for item in perguntas:
            nome_do_quiz = item.quiz
            id_quiz = self.kwargs.get('pk')
            respostas_corretas.append(item.respostaCorreta)
        tamanho_lista = len(respostas_corretas)
        acertos, erros, total = 0, 0, 0
        for indice in range(tamanho_lista):
            if respostas_usuario[indice] == respostas_corretas[indice]:
                acertos += 1
                total += 1
            else:
                erros += 1
                total += 1
        print(acertos, erros)
        return render(request, 'resultado.html', {'erros': erros, 'acertos': acertos, 'total': total, 'quiz': nome_do_quiz, 'id_quiz': id_quiz})


def login(request):
    verifica_url(request)
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        usernameOrEmail = request.POST.get('usuarioOuEmail')
        senha = request.POST.get('senha')

        userVerify = authenticate(username=usernameOrEmail, password=senha) or authenticate(email=usernameOrEmail, password=senha)

        if userVerify:
            login_django(request, userVerify)
            return redirect('animes:home')
        else:
            return render(request, 'login.html', {'erro': 'Ocorreu um erro no login'})

def cadastro(request):
    verifica_url(request)
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else:
        usuario = request.POST.get('usuario')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        userVerifyUsername = User.objects.filter(username=usuario).first()
        userVerifyEmail = User.objects.filter(email=email).first()
        if userVerifyUsername or userVerifyEmail:
            return render(request, 'cadastro.html', {'erro': 'Usuário já existente'})
        else:
            newUser = User.objects.create_user(
                username=usuario,
                email=email,
                password=senha
            )
            newUser.save()
            return redirect('animes:login')



class MeusQuizes(LoginRequiredMixin, ListView):
    template_name = 'meus-quizes.html'
    model = Quiz

    def post(self, request, *args, **kwargs):
        verifica_url(request)
        nome_quiz = request.POST.get('nome_pesquisa_quiz')
        lista_quiz = Quiz.objects.filter(nome__icontains=nome_quiz, usuario=request.user)
    
        return render(request, self.template_name, {"object_list": lista_quiz})
    
    def get_queryset(self):
        return Quiz.objects.filter(usuario=self.request.user)


        


def excluir_quiz(request, quiz_id):
    verifica_url(request)
    if request.method == "DELETE":
        quiz = get_object_or_404(Quiz, id=quiz_id)
        quiz.delete()
        return JsonResponse({"success": True})
    else:
        return JsonResponse({"success": False})