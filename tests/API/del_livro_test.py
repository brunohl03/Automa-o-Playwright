from playwright.sync_api import sync_playwright  # importa Playwright
import random  # importa random
import json  # importa json

def gerar_usuario():  # função para gerar usuário
    return f"user_{random.randint(1000,9999)}"  # retorna username único

def test_deletar_livro():  # teste para deletar livro específico
    username = gerar_usuario()  # gera username
    password = "Abc#0123"  # define senha

    with sync_playwright() as p:  # inicia Playwright
        request = p.request.new_context()  # cria contexto HTTP

        payload = {"userName": username, "password": password}  # cria payload

        create = request.post("https://demoqa.com/Account/v1/User", data=json.dumps(payload), headers={"Content-Type": "application/json"})  # cria usuário
        user_id = create.json()["userID"]  # captura UUID

        token = request.post("https://demoqa.com/Account/v1/GenerateToken", data=json.dumps(payload), headers={"Content-Type": "application/json"}).json()["token"]  # gera token

        books = request.get("https://demoqa.com/BookStore/v1/Books").json()  # lista livros
        isbn = books["books"][0]["isbn"]  # pega ISBN

        request.post("https://demoqa.com/BookStore/v1/Books", data=json.dumps({"userId": user_id, "collectionOfIsbns": [{"isbn": isbn}]}), headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"})  # adiciona livro

        delete_resp = request.delete("https://demoqa.com/BookStore/v1/Book", data=json.dumps({"isbn": isbn, "userId": user_id}), headers={"Content-Type": "application/json", "Authorization": f"Bearer {token}"})  # deleta livro

        assert delete_resp.status == 204  # valida que o livro foi deletado com sucesso