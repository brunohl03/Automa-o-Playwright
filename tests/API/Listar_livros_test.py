from playwright.sync_api import sync_playwright  # importa o Playwright para requisições HTTP

def test_listar_livros():  # função de teste para listar livros
    with sync_playwright() as p:  # inicia contexto do Playwright
        request = p.request.new_context()  # cria contexto de requisição HTTP

        response = request.get("https://demoqa.com/BookStore/v1/Books")  # faz GET para listar livros

        assert response.status == 200  # valida que a requisição retornou sucesso
        body = response.json()  # converte resposta para JSON
        assert "books" in body  # valida que existe a chave 'books'
        assert len(body["books"]) > 0  # valida que existe pelo menos um livro

        print("Livros disponíveis:", body["books"])  # imprime lista de livros