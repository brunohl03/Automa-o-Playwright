from playwright.sync_api import sync_playwright  # importa Playwright
import random  # importa random
import json  # importa json

def gerar_usuario():  # gera usuário único
    return f"user_{random.randint(1000,9999)}"  # retorna username aleatório

def test_deletar_todos_livros():  # teste para deletar todos os livros do usuário
    username = gerar_usuario()  # gera usuário
    password = "Abc#0123"  # define senha

    with sync_playwright() as p:  # inicia Playwright
        request = p.request.new_context()  # cria contexto HTTP

        payload = {"userName": username, "password": password}  # cria payload

        create = request.post("https://demoqa.com/Account/v1/User", data=json.dumps(payload), headers={"Content-Type": "application/json"})  # cria usuário
        assert create.status == 201  # valida criação
        user_id = create.json()["userID"]  # captura UUID

        token = request.post("https://demoqa.com/Account/v1/GenerateToken", data=json.dumps(payload), headers={"Content-Type": "application/json"}).json()["token"]  # gera token

        books = request.get("https://demoqa.com/BookStore/v1/Books").json()  # lista livros
        isbn = books["books"][0]["isbn"]  # pega ISBN

        request.post("https://demoqa.com/BookStore/v1/Books", data=json.dumps({"userId": user_id, "collectionOfIsbns": [{"isbn": isbn}]}), headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"})  # adiciona livro ao usuário

        delete_resp = request.delete(f"https://demoqa.com/BookStore/v1/Books?UserId={user_id}", headers={"Authorization": f"Bearer {token}"})  # deleta todos os livros do usuário

        assert delete_resp.status == 204  # valida que todos os livros foram deletados

        print("Todos os livros foram deletados com sucesso")  # log