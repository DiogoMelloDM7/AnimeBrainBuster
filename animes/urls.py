from django.urls import path
from .views import Home, criarQuiz, pesquisarQuiz, login

app_name = 'animes'

urlpatterns=[
    path('', Home.as_view(), name='home'),
    path('criarquiz', criarQuiz, name="criarquiz"),
    path('pesquisarquiz', pesquisarQuiz, name="pesquisarquiz"),
    path('login', login, name='login'),
]