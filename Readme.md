# Projeto de Automação - DemoQA

Este projeto tem como objetivo realizar testes automatizados na plataforma DemoQA utilizando Python, Playwright, Pytest e BDD (Gherkin). O foco é automatizar cenários funcionais da aplicação para validar comportamentos da interface, fluxos de usuário e interações com elementos da página. A aplicação utilizada para testes é: https://demoqa.com/

Estrutura do projeto:

## Estrutura do Projeto

```bash
automation-project/
├── features/
│   └── login.feature
├── tests/
│   └── steps/
│       └── test_login_steps.py
├── pages/
│   └── login_page.py
├── utils/
│   ├── helpers.py
│   └── data_generator.py
├── screenshots/
├── reports/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

O projeto segue o padrão Page Object Model, com separação de cenários BDD, implementação de steps, utilitários auxiliares, evidências de falha e relatórios de execução.

Para configurar o ambiente, crie um ambiente virtual com o comando:

python -m venv venv

Ative o ambiente virtual:

venv\Scripts\activate

As dependências estão definidas no arquivo requirements.txt: playwright (automação de navegador), pytest (framework de testes), pytest-playwright (integração Playwright + Pytest), allure-pytest (geração de relatórios), pytest-bdd (suporte à linguagem Gherkin).

Instale as dependências:

pip install -r requirements.txt

Instale os navegadores do Playwright:

playwright install

Para executar os testes:

pytest

Para executar exibindo o navegador e logs detalhados:

pytest --headed -v

Para executar gerando resultados para o Allure:

pytest --alluredir=allure-results --headed -v

Para abrir o relatório interativo:

allure serve allure-results

Projeto desenvolvido para fins de estudo e prática profissional em automação de testes.