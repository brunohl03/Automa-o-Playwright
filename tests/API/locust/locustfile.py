from locust import HttpUser, task, between
import random
import json

class UsuarioDemoQA(HttpUser):
    wait_time = between(1, 2)  # espera entre ações do usuário

    @task
    def criar_gerar_buscar_deletar(self):
        username = f"user_{random.randint(1000,9999)}"  # gera usuário aleatório
        password = "Abc#0123"  # senha fixa
        payload = {"userName": username, "password": password}  # payload para API

        headers = {"Accept": "application/json"}  # header para evitar 406

        # 1️⃣ Cria usuário
        resp = self.client.post("/Account/v1/User", json=payload, headers=headers)  # POST para criar usuário
        if resp.status_code == 201:
            user_id = resp.json()["userID"]  # captura UUID
            print(f"Usuário criado: {username}, UUID: {user_id}")
        else:
            print(f"Falha ao criar usuário {username}, status {resp.status_code}")
            return  # aborta se não criar

"""
        # 2️⃣ Gera token
        resp_token = self.client.post("/Account/v1/GenerateToken", json=payload, headers=headers)  # POST para gerar token
        if resp_token.status_code == 200:
            token = resp_token.json().get("token", "")
            print(f"Token gerado para {username}: {token}")
        else:
            print(f"Falha ao gerar token para {username}, status {resp_token.status_code}")
            return  # aborta se não gerar token

        # 3️⃣ Busca usuário
        if token:
            search_resp = self.client.get(f"/Account/v1/User/{user_id}", headers={**headers, "Authorization": f"Bearer {token}"})  # GET com token
            if search_resp.status_code == 200:
                user_data = search_resp.json()
                print(f"Usuário buscado com sucesso: {user_data}")
            else:
                print(f"Falha ao buscar usuário {username}, status {search_resp.status_code}")

        # 4️⃣ Deleta usuário (opcional)
        delete_resp = self.client.delete(f"/Account/v1/User/{user_id}", headers={**headers, "Authorization": f"Bearer {token}"})  # DELETE com token
        if delete_resp.status_code == 204:
            print(f"Usuário {username} deletado com sucesso!")
        else:
            print(f"Falha ao deletar usuário {username}, status {delete_resp.status_code}")

"""