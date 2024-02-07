# AnimesBrainBuster: Uma plataforma de Quizes

# Sobre o Projeto

AnimesBrainBuster é uma plataforma cujo foco é apenas o entretenimento, crie e participe de quizes, testando seu conhecimento e dos outros usuários. [Visualize a aplicação aqui](https://animebrainbuster-production.up.railway.app/).

## Funcionalidades

* Criação de quizes.
* Participe de quizes criados por outros usuários.
  
OBS: Para utilizar dessas funcionalidades o usuário deverá estar logado a plataforma.

# Tecnologias

## Back-End
* Python
* Django

## Front-End
* HTML5 / CSS3
* JavaScript

## Banco de Dados
* PostgreSQL


## HomePage
![AnimesBrainbuster-home](https://github.com/DiogoMelloDM7/AnimeBrainBuster/assets/136912625/d674599e-ceb9-4416-9272-f579c41d71b1)

## Baixando e rodando a aplicação localmente

Para começar, siga estas etapas para baixar o código-fonte do projeto localmente:

1. Abra o terminal no seu computador.
2. Navegue até o diretório onde deseja armazenar o projeto.
3. Use o seguinte comando para clonar o repositório:

```bash
git clone https://github.com/DiogoMelloDM7/AnimeBrainBuster.git
```

### Configurando ambiente

Antes de executar a aplicação localmente, você precisa configurar o ambiente. Siga estas etapas:

1. Abra o terminal e navegue até o diretório raiz do projeto.
2. Execute o seguinte comando para instalar as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Executando a aplicação localmente

Após a configuração do ambiente, você pode iniciar a aplicação localmente. Siga estas etapas:

1. No terminal, navegue até o diretório raiz do projeto.
2. Execute o seguinte comando para aplicar migrações do banco de dados, se necessário:

```bash
python manage.py migrate
```

1. Inicie o servidor de desenvolvimento com o seguinte comando:

```bash
python manage.py runserver
```












