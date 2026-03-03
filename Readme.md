# Projeto de Automação - DemoQA

Este projeto tem como objetivo realizar testes automatizados na plataforma DemoQA utilizando:

- Python
- Playwright
- Pytest
- BDD (Gherkin)

## Objetivo

Automatizar cenários funcionais da aplicação DemoQA para validar comportamentos da interface, fluxos de usuário e interações com elementos da página.

A aplicação utilizada para testes é:
https://demoqa.com/

## Estrutura do Projeto

automation-project/
│
├── features/         # Cenários escritos em Gherkin
├── tests/            # Implementação dos steps
├── pages/            # Page Object Model
├── utils/            # Funções auxiliares
├── screenshots/      # Prints em caso de falha
├── reports/          # Relatórios de execução
├── conftest.py       # Configuração global e fixtures
├── pytest.ini        # Configuração do pytest
├── requirements.txt  # Dependências do projeto
├── .gitignore
└── README.md

## Configuração do Ambiente

### Criar e ativar ambiente virtual

python -m venv venv  
Cria um ambiente virtual para o projeto.

venv\Scripts\activate  
Ativa o ambiente virtual e isola as bibliotecas do projeto.

## Dependências (requirements.txt)

playwright  
Biblioteca de automação de navegador.

pytest  
Framework para execução de testes.

pytest-playwright  
Integração do Playwright com o Pytest.

allure-pytest  
Integração do Allure para geração de relatórios.

pytest-bdd  
Adiciona suporte à linguagem BDD (Gherkin).

## Instalação das Dependências

pip install -r requirements.txt  
Instala todas as dependências do projeto.

playwright install  
Instala os navegadores usados pelo Playwright.

## Execução dos Testes

pytest  
Executa os testes.

pytest --headed -v  
Executa os testes abrindo o navegador e exibindo logs detalhados.

pytest --alluredir=allure-results --headed -v  
Executa os testes e gera os resultados para o relatório Allure.

allure serve allure-results  
Gera e abre o relatório interativo do Allure.