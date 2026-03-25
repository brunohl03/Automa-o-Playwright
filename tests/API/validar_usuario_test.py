from playwright.sync_api import sync_playwright  # importa Playwright para usar requests HTTP
import random  # importa random para gerar números aleatórios
import json  # importa json para converter dict em JSON

def gerar_usuario():  # função para gerar nome de usuário único
    return f"user_{random.randint(10000,99999)}"  # retorna "user_" + número aleatório (range maior para evitar duplicidade)

def test_authorized_user():  # teste para verificar autorização do usuário
    with sync_playwright() as p:  # abre contexto Playwright
        request = p.request.new_context(  # cria contexto de requisições HTTP
            extra_http_headers={  # define headers padrão para todas requisições
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        )

        username = gerar_usuario()  # gera usuário aleatório
        password = "Abc#0123"  # define senha fixa

        # 1️⃣ Cria usuário
        payload = {"userName": username, "password": password}  # payload para criar usuário
        create_resp = request.post(
            f"https://demoqa.com/Account/v1/User",
            data=json.dumps(payload)  # ✅ CORRETO para sua versão
        )
        assert create_resp.status == 201, create_resp.text()  # verifica se usuário foi criado com sucesso
        print(f"Usuário criado: {username}")  # imprime nome do usuário criado

        # 2️⃣ Valida autorização do usuário
        auth_resp = request.post(
            f"https://demoqa.com/Account/v1/Authorized",
            data=json.dumps(payload)  # ✅ CORRETO para sua versão
        )
        assert auth_resp.status == 200, auth_resp.text()  # verifica se a autorização retornou 200
        print(f"Usuário {username} autorizado com sucesso!")  # imprime confirmação da autorização