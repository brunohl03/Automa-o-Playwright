from playwright.sync_api import sync_playwright  # importa Playwright para usar requests HTTP
import random  # importa random para gerar números aleatórios
import json  # importa json para converter dict em JSON

def gerar_usuario():  # função para gerar nome de usuário único
    return f"user_{random.randint(1000,9999)}"  # retorna "user_" + número aleatório

def test_criar_gerar_buscar_usuario():  # define o teste principal
    username = gerar_usuario()  # gera usuário aleatório
    password = "Abc#0123"  # define senha fixa

    with sync_playwright() as p:  # abre contexto Playwright
        request = p.request.new_context()  # cria contexto de requisições HTTP

        # 1️⃣ Cria usuário
        payload = {"userName": username, "password": password}  # payload para criar usuário
        create_resp = request.post("https://demoqa.com/Account/v1/User", data=json.dumps(payload), headers={"Content-Type": "application/json"})  # faz POST para criar usuário
        assert create_resp.status == 201  # verifica se o usuário foi criado com sucesso
        body = create_resp.json()  # converte resposta em JSON
        user_id = body["userID"]  # captura UUID do usuário criado
        print(f"Usuário criado: {username}, UUID: {user_id}")  # imprime usuário criado e UUID

        # 2️⃣ Gera token
        token_resp = request.post("https://demoqa.com/Account/v1/GenerateToken", data=json.dumps(payload), headers={"Content-Type": "application/json"})  # faz POST para gerar token usando mesmo payload de usuário
        assert token_resp.status == 200  # verifica se token foi gerado com sucesso
        token = token_resp.json()["token"]  # captura token da resposta
        print(f"Token gerado: {token}")  # imprime token gerado

        # 3️⃣ Busca usuário pelo UUID com token
        search_resp = request.get(f"https://demoqa.com/Account/v1/User/{user_id}", headers={"Authorization": f"Bearer {token}"})  # faz GET para buscar usuário usando UUID e token no header
        assert search_resp.status == 200  # verifica se busca foi autorizada e retornou 200
        user_data = search_resp.json()  # converte resposta em JSON
        assert user_data["username"] == username  # valida que o nome retornado é igual ao criado
        print("Dados do usuário encontrados:", user_data)  # imprime os dados completos do usuário