from playwright.sync_api import sync_playwright  # importa Playwright para usar requests HTTP
import random  # importa random para gerar números aleatórios

def gerar_usuario():  # função para gerar nome de usuário único
    return f"user_{random.randint(1000,9999)}"  # retorna "user_" + número aleatório

def test_authorized_user():  # teste para verificar autorização do usuário
    with sync_playwright() as p:  # abre contexto Playwright
        request = p.request.new_context()  # cria contexto de requisições HTTP

        username = gerar_usuario()  # gera usuário aleatório
        password = "Abc#0123"  # define senha fixa

        # 1️⃣ Cria usuário
        create_resp = request.post(f"https://demoqa.com/Account/v1/User", data={"userName": username, "password": password})  # faz POST para criar usuário
        assert create_resp.status == 201  # verifica se usuário foi criado com sucesso
        print(f"Usuário criado: {username}")  # imprime nome do usuário criado

        # 2️⃣ Valida autorização do usuário
        auth_resp = request.post(f"https://demoqa.com/Account/v1/Authorized", data={"userName": username, "password": password})  # faz POST para verificar se usuário está autorizado
        assert auth_resp.status == 200  # verifica se a autorização retornou 200
        print(f"Usuário {username} autorizado com sucesso!")  # imprime confirmação da autorização