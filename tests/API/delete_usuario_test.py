from playwright.sync_api import sync_playwright  # importa Playwright para usar requests HTTP
import random  # importa random para gerar números aleatórios
import json  # importa json para converter dict em JSON

def gerar_usuario():  # função para gerar nome de usuário único
    return f"user_{random.randint(10000,99999)}"  # retorna "user_" + número aleatório (range maior para evitar duplicidade)

def test_fluxo_completo_usuario():  # teste completo do fluxo do usuário
    username = gerar_usuario()  # gera usuário aleatório
    password = "Abc#0123"  # define senha fixa

    with sync_playwright() as p:  # abre contexto Playwright
        request = p.request.new_context(  # cria contexto de requisições HTTP
            extra_http_headers={  # define headers padrão para todas requisições
                "Content-Type": "application/json",
                "Accept": "application/json"
            }
        )

        # 1️⃣ Cria usuário
        payload = {"userName": username, "password": password}  # payload para criar usuário
        create_resp = request.post(f"https://demoqa.com/Account/v1/User", data=json.dumps(payload))  # faz POST para criar usuário usando JSON
        assert create_resp.status == 201, create_resp.text()  # verifica se usuário foi criado com sucesso
        user_id = create_resp.json()["userID"]  # captura UUID do usuário criado
        print(f"Usuário criado: {username}, UUID: {user_id}")  # imprime usuário e UUID

        # 2️⃣ Gera token
        token_resp = request.post(f"https://demoqa.com/Account/v1/GenerateToken", data=json.dumps(payload))  # faz POST para gerar token usando JSON
        assert token_resp.status == 200, token_resp.text()  # verifica se token foi gerado com sucesso
        token = token_resp.json()["token"]  # captura token JWT
        print(f"Token gerado: {token}")  # imprime token gerado

        # 3️⃣ Busca usuário pelo UUID com token
        search_resp = request.get(f"https://demoqa.com/Account/v1/User/{user_id}", headers={"Authorization": f"Bearer {token}"})  # faz GET para buscar usuário usando UUID e token no header
        assert search_resp.status == 200, search_resp.text()  # verifica se busca foi autorizada e retornou 200
        user_data = search_resp.json()  # converte resposta em JSON
        assert user_data["username"] == username  # valida que o nome retornado é igual ao criado
        print("Dados do usuário encontrados:", user_data)  # imprime os dados completos do usuário

        # 4️⃣ Deleta usuário pelo UUID com token
        delete_resp = request.delete(f"https://demoqa.com/Account/v1/User/{user_id}", headers={"Authorization": f"Bearer {token}"})  # faz DELETE para remover usuário usando UUID e token no header
        assert delete_resp.status == 204, delete_resp.text()  # verifica se usuário foi deletado com sucesso (204 No Content)
        print(f"Usuário {username} deletado com sucesso!")  # imprime confirmação da exclusão

        # 5️⃣ Valida exclusão tentando buscar usuário
        search_resp = request.get(f"https://demoqa.com/Account/v1/User/{user_id}", headers={"Authorization": f"Bearer {token}"})  # tenta buscar usuário deletado usando UUID e token no header
        assert search_resp.status == 401, search_resp.text()  # valida que o usuário não existe mais (401 Unauthorized)
        print(f"Validação: usuário {username} não existe mais (status {search_resp.status})")  # imprime resultado da validação