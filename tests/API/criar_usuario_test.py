from playwright.sync_api import sync_playwright  # importa Playwright para usar requests HTTP
import random  # importa random para gerar números aleatórios
import json  # importa json para converter dict em JSON

def gerar_usuario():  # função para gerar nome de usuário único
    return f"user_{random.randint(1000,9999)}"  # retorna "user_" + número aleatório

def test_fluxo_completo_usuario():  # teste completo do fluxo do usuário
    username = gerar_usuario()  # gera usuário aleatório
    password = "Abc#0123"  # define senha fixa

    with sync_playwright() as p:  # abre contexto Playwright
        request = p.request.new_context()  # cria contexto de requisições HTTP

        # 1️⃣ Cria usuário
        payload = {"userName": username, "password": password}  # payload para criar usuário
        create_resp = request.post(f"https://demoqa.com/Account/v1/User", data=json.dumps(payload), headers={"Content-Type": "application/json"})  # faz POST para criar usuário
        assert create_resp.status == 201  # verifica se usuário foi criado com sucesso
        user_id = create_resp.json()["userID"]  # captura UUID do usuário criado
        print(f"Usuário criado: {username}, UUID: {user_id}")  # imprime usuário e UUID