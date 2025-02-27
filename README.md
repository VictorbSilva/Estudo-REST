# Estudo-REST
Projeto simples usando CRUD em django e django rest framework

Estrutura do Projeto

O projeto é composto pelos seguintes arquivos e diretórios:

    apps.py: Configuração do aplicativo bookstore.

    models.py: Define o modelo Book para armazenar informações sobre os livros.

    serializers.py: Serializa e desserializa os dados do modelo Book para JSON e vice-versa.

    tests.py: Local para escrever testes automatizados (atualmente vazio).

    urls.py: Define as rotas da API para o aplicativo bookstore.

    views.py: Arquivo para views baseadas em funções (atualmente vazio).

    viewsets.py: Define a BookViewSet, que fornece operações CRUD para o modelo Book.

Funcionalidades
1. Modelo Book

O modelo Book representa um livro no banco de dados e possui os seguintes campos:

    id_book: Um UUID único que serve como chave primária.

    title: Título do livro (campo de texto com limite de 100 caracteres).

    author: Autor do livro (campo de texto com limite de 100 caracteres).

O método __str__ retorna uma representação legível do livro, incluindo título, autor e ID.
2. Serializador BookSerializer

O BookSerializer é responsável por converter instâncias do modelo Book em JSON e vice-versa. Ele usa a classe ModelSerializer do Django REST Framework para serializar todos os campos do modelo.
3. ViewSet BookViewSet

A BookViewSet é uma classe que fornece operações CRUD para o modelo Book. Ela utiliza o ModelViewSet do Django REST Framework, que automaticamente implementa as seguintes ações:

    Listar todos os livros (GET /bookstore/)

    Criar um novo livro (POST /bookstore/)

    Recuperar um livro específico (GET /bookstore/<id>/)

    Atualizar um livro (PUT /bookstore/<id>/ ou PATCH /bookstore/<id>/)

    Excluir um livro (DELETE /bookstore/<id>/)

4. Rotas da API

As rotas da API são configuradas no arquivo urls.py usando o SimpleRouter do Django REST Framework. Ele registra automaticamente as rotas para as operações CRUD da BookViewSet.
Como Usar
1. Instalação

    Clone o repositório do projeto.

    Crie e ative um ambiente virtual:
    bash
    Copy

    python -m venv venv
    source venv/bin/activate  # No macOS/Linux
    venv\Scripts\activate     # No Windows

    Instale as dependências:
    bash
    Copy

    pip install django djangorestframework

    Execute as migrações para criar o banco de dados:
    bash
    Copy

    python manage.py migrate

2. Executando o Projeto

    Inicie o servidor de desenvolvimento:
    bash
    Copy

    python manage.py runserver

    Acesse a API no navegador ou usando uma ferramenta como o Postman:

        URL base: http://127.0.0.1:8000/bookstore/

3. Endpoints da API

    Listar todos os livros:

        Método: GET

        URL: http://127.0.0.1:8000/bookstore/

        Exemplo de resposta:
        json
        Copy

        [
            {
                "id_book": "550e8400-e29b-41d4-a716-446655440000",
                "title": "1984",
                "author": "George Orwell"
            },
            {
                "id_book": "550e8400-e29b-41d4-a716-446655440001",
                "title": "O Senhor dos Anéis",
                "author": "J.R.R. Tolkien"
            }
        ]

    Criar um novo livro:

        Método: POST

        URL: http://127.0.0.1:8000/bookstore/

        Corpo da requisição (JSON):
        json
        Copy

        {
            "title": "Dom Quixote",
            "author": "Miguel de Cervantes"
        }

        Exemplo de resposta:
        json
        Copy

        {
            "id_book": "550e8400-e29b-41d4-a716-446655440002",
            "title": "Dom Quixote",
            "author": "Miguel de Cervantes"
        }

    Recuperar um livro específico:

        Método: GET

        URL: http://127.0.0.1:8000/bookstore/<id_book>/

        Exemplo de resposta:
        json
        Copy

        {
            "id_book": "550e8400-e29b-41d4-a716-446655440000",
            "title": "1984",
            "author": "George Orwell"
        }

    Atualizar um livro:

        Método: PUT ou PATCH

        URL: http://127.0.0.1:8000/bookstore/<id_book>/

        Corpo da requisição (JSON):
        json
        Copy

        {
            "title": "1984",
            "author": "George Orwell (Updated)"
        }

        Exemplo de resposta:
        json
        Copy

        {
            "id_book": "550e8400-e29b-41d4-a716-446655440000",
            "title": "1984",
            "author": "George Orwell (Updated)"
        }

    Excluir um livro:

        Método: DELETE

        URL: http://127.0.0.1:8000/bookstore/<id_book>/

        Resposta: Status 204 No Content.
