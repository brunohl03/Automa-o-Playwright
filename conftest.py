"""
conftest.py

Este arquivo é usado pelo pytest para centralizar **fixtures, setups e configurações globais**
do projeto de testes.  

Ele permite criar recursos que serão usados em vários testes de forma automática, 
como navegadores, páginas iniciais, usuários falsos, dados aleatórios, logs ou relatórios.  

Objetivos principais:
- Compartilhar dados ou objetos entre testes sem precisar importar manualmente.
- Organizar e padronizar setups e teardowns (abrir/fechar navegador, limpar dados, etc.).
- Configurar comportamentos globais do pytest, como paralelismo, relatórios e opções de execução.
- Facilitar a manutenção e tornar os testes mais legíveis e didáticos para quem for aprender automação.

Exemplo de uso: fixtures que retornam um usuário fake, que já podem ser injetadas diretamente
nos testes.

"""

# conftest.py
from pytest_bdd import given

@given("que o usuário acessa a página inicial")
def acessar_home(page):
    page.goto("https://demoqa.com/")
    page.evaluate("document.body.style.zoom='50%'")