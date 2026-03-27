from playwright.sync_api import sync_playwright  # importa Playwright
import random  # importa random
import json  # importa json

def gerar_usuario():  # gera usuário
    return f"user_{random.randint(1000,9999)}"  # retorna username

def test_buscar_livros_usuario():  # teste de busca
    username = gerar_usuario()  # gera usuário
    password = "Abc#0123"  # senha

    with sync_playwright() as p:  # inicia Playwright
        request = p.request.new_context()  # contexto HTTP

        payload = {"userName": username, "password": password}  # payload

        create = request.post("https://demoqa.com/Account/v1/User", data=json.dumps(payload), headers={"Content-Type": "application/json", "Accept": "application/json"})  # cria usuário com headers completos
        assert create.status == 201  # valida criação do usuário
        create_body = create.json()  # converte resposta em JSON
        assert "userID" in create_body  # valida existência do userID
        user_id = create_body["userID"]  # UUID

        token_resp = request.post("https://demoqa.com/Account/v1/GenerateToken", data=json.dumps(payload), headers={"Content-Type": "application/json", "Accept": "application/json"})  # gera token
        assert token_resp.status == 200  # valida geração do token
        token_body = token_resp.json()  # converte resposta
        assert "token" in token_body  # valida existência do token
        token = token_body["token"]  # captura token

        books_resp = request.get("https://demoqa.com/BookStore/v1/Books")  # busca livros disponíveis
        assert books_resp.status == 200  # valida sucesso
        books = books_resp.json()  # converte resposta
        assert len(books["books"]) > 0  # valida que há livros
        isbn = books["books"][0]["isbn"]  # ISBN

        add_resp = request.post("https://demoqa.com/BookStore/v1/Books", data=json.dumps({"userId": user_id, "collectionOfIsbns": [{"isbn": isbn}]}), headers={"Content-Type": "application/json", "Accept": "application/json", "Authorization": f"Bearer {token}"})  # adiciona livro
        assert add_resp.status == 201  # valida adição do livro

        response = request.get(f"https://demoqa.com/Account/v1/User/{user_id}", headers={"Authorization": f"Bearer {token}"})  # busca usuário

        assert response.status == 200  # valida sucesso
        body = response.json()  # converte resposta
        assert "books" in body  # valida existência da lista de livros
        assert len(body["books"]) > 0  # valida que usuário possui livros