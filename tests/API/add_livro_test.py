from playwright.sync_api import sync_playwright  # importa Playwright
import random  # importa biblioteca para gerar valores aleatórios
import json  # importa biblioteca para manipular JSON

def gerar_usuario():  # função para gerar username único
    return f"user_{random.randint(1000,9999)}"  # retorna username aleatório

def test_adicionar_livro():  # função de teste para adicionar livro
    username = gerar_usuario()  # gera username único
    password = "Abc#0123"  # define senha padrão

    with sync_playwright() as p:  # inicia Playwright
        request = p.request.new_context()  # cria contexto de requisição

        payload = {"userName": username, "password": password}  # cria payload para usuário

        create = request.post("https://demoqa.com/Account/v1/User", data=json.dumps(payload), headers={"Content-Type": "application/json", "Accept": "application/json"})  # cria usuário via POST com headers completos
        assert create.status == 201  # valida que usuário foi criado com sucesso
        body = create.json()  # converte resposta em JSON
        assert "userID" in body  # valida que userID existe na resposta
        user_id = body["userID"]  # captura UUID do usuário

        token_resp = request.post("https://demoqa.com/Account/v1/GenerateToken", data=json.dumps(payload), headers={"Content-Type": "application/json", "Accept": "application/json"})  # gera token com headers completos
        assert token_resp.status == 200  # valida sucesso da geração do token
        token_body = token_resp.json()  # converte resposta
        assert "token" in token_body  # valida existência do token
        token = token_body["token"]  # captura token

        books_resp = request.get("https://demoqa.com/BookStore/v1/Books")  # faz GET para listar livros disponíveis
        assert books_resp.status == 200  # valida sucesso da listagem
        books = books_resp.json()  # converte resposta em JSON
        assert len(books["books"]) > 0  # valida que existe pelo menos um livro
        isbn = books["books"][0]["isbn"]  # pega ISBN do primeiro livro

        add_resp = request.post("https://demoqa.com/BookStore/v1/Books", data=json.dumps({"userId": user_id, "collectionOfIsbns": [{"isbn": isbn}]}), headers={"Content-Type": "application/json", "Accept": "application/json", "Authorization": f"Bearer {token}"})  # adiciona livro ao usuário com token

        assert add_resp.status == 201  # valida sucesso da adição do livro