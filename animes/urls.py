from django.urls import path
from .views import Home, criarQuiz, PesquisarQuiz, login, QuizIndividual, cadastro, MeusQuizes, excluir_quiz
from django.contrib.auth import views as auth_views

app_name = 'animes'

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('criarquiz', criarQuiz, name="criarquiz"),
    path('pesquisarquiz', PesquisarQuiz.as_view(), name="pesquisarquiz"),
    path('login', login, name='login'),
    path('quizindividual/<int:pk>',QuizIndividual.as_view(), name='quizIndividual'),
    path('cadastro', cadastro, name="cadastro"),
    path('logout', auth_views.LogoutView.as_view(template_name='login.html'),name='logout'),
    path('meusquizes', MeusQuizes.as_view(), name="meusquizes"),
    path('excluirquiz/<int:quiz_id>', excluir_quiz, name='excluirquiz'),
]