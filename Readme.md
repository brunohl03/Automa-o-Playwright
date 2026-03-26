# Projeto de Automação - DemoQA

Este projeto tem como objetivo realizar testes automatizados na plataforma DemoQA utilizando Python, Playwright, Pytest e BDD (Gherkin). O foco é automatizar cenários funcionais da aplicação para validar comportamentos da interface, fluxos de usuário e interações com elementos da página. A aplicação utilizada para testes é: https://demoqa.com/

Estrutura do projeto:

## Estrutura do Projeto

```bash
Automa-o-Playwright/
│
├── .github/
│   ├── workflows/
│   │   └── CI.yml
│   └── ISSUE_TEMPLATE/
│       └── bug_report.md
│
├── features/
│   ├── text_box.feature
│   ├── check_box.feature
│   ├── radio_button.feature
│   ├── web_tables.feature
│   ├── buttons.feature
│   ├── links.feature
│   ├── broken_links.feature
│   ├── upload_download.feature
│   └── dynamic_properties.feature
│
├── pages/
│   ├── text_box_page.py
│   ├── check_box_page.py
│   ├── radio_button_page.py
│   ├── web_tables_page.py
│   ├── buttons_page.py
│   ├── links_page.py
│   ├── broken_links_page.py
│   ├── upload_download_page.py
│   ├── dynamic_properties_page.py
│   └── __init__.py
│
├── steps/
│   ├── text_box_steps.py
│   ├── check_box_steps.py
│   ├── radio_button_steps.py
│   ├── web_tables_steps.py
│   ├── buttons_steps.py
│   ├── links_steps.py
│   ├── broken_links_steps.py
│   ├── upload_download_steps.py
│   ├── dynamic_properties_steps.py
│   └── __init__.py
│
├── tests/
│   ├── text_box_test.py
│   ├── check_box_test.py
│   ├── radio_button_test.py
│   ├── web_tables_test.py
│   ├── buttons_test.py
│   ├── links_test.py
│   ├── broken_links_test.py
│   ├── upload_download_test.py
│   ├── dynamic_properties_test.py
│   ├── API/
│   │   ├── buscar_usuario_test.py
│   │   ├── criar_usuario_test.py
│   │   ├── delete_usuario_test.py
│   │   ├── gerar_token_test.py
│   │   ├── validar_usuario_test.py
│   │   └── locust/
│   │       └── locustfile.py
│   └── __init__.py
│
├── utils/
│   ├── helpers.py
│   ├── data_generator.py
│   ├── screenshots/
│   ├── upload_images/
│   └── __init__.py
│
├── config/
│   ├── settings.py
│   └── __init__.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── requisitos.md
├── .gitignore
└── README.md
```

## Documentação de Requisitos

Foi criado o arquivo ```requisitos.md ``` com o objetivo de documentar os requisitos funcionais e não funcionais da aba Elements da aplicação. Este documento serve como base para a definição dos cenários BDD e auxilia na rastreabilidade entre as regras de negócio e os testes automatizados implementados no projeto.

## Teste de Performance

Além dos testes funcionais automatizados com Playwright e Pytest, o projeto inclui testes de performance utilizando **Locust**, uma ferramenta desenvolvida em Python para simular múltiplos usuários e medir a performance da API da DemoQA.

### Estrutura do Script

O script de performance é responsável por simular o comportamento de usuários virtuais realizando um conjunto de ações sobre a aplicação. Cada usuário virtual pode executar um **ciclo de interações**, que representa o fluxo típico de uso da aplicação.

O Locust registra métricas detalhadas para cada requisição dentro do ciclo, permitindo analisar:

- **Requests per Second (RPS)** → quantas requisições estão sendo processadas por segundo.
- **Response Times** → tempo médio, mínimo e máximo das requisições.
- **Failures** → quantas requisições falharam durante o teste.
- **Ciclos completos** → tempo total para execução de todas as ações de um usuário virtual.

Essa abordagem permite avaliar a performance da aplicação sob carga, identificar gargalos e medir o comportamento de diferentes endpoints ou fluxos completos de usuários.

O projeto segue o padrão Page Object Model, com separação de cenários BDD, implementação de steps, utilitários auxiliares, evidências de falha e relatórios de execução.

Para configurar o ambiente, crie um ambiente virtual com o comando:
```bash
python -m venv venv
```
Ative o ambiente virtual:
```bash
venv\Scripts\activate
```
As dependências estão definidas no arquivo requirements.txt:

- **pytest** → Framework para execução de testes.  
- **pytest-playwright** → Integração do Playwright com o Pytest.  
- **allure-pytest** → Integração do Allure para geração de relatórios.  
- **pytest-bdd** → Adiciona suporte à linguagem BDD aos testes.  
- **pytest-rerunfailures** → Permite reexecutar testes que falharam.  
- **pytest-xdist** → Permite a execução de testes em paralelo.  
- **faker** → Biblioteca para geração de dados falsos, útil para testes.  
- **locust** → Ferramenta de teste de carga para simular múltiplos usuários.  
- **playwright** → Automação de navegadores para testes end-to-end.

Instale as dependências:
```bash
pip install -r requirements.txt
```
Instale os navegadores do Playwright:
```bash
playwright install
```
Para executar os testes:
```bash
pytest
```
Para executar exibindo o navegador e logs detalhados:
```bash
pytest --headed
```
Para abrir o relatório interativo:
```bash
allure serve allure-results
```
Para rodar o Locust e acessar o painel web (direcionar terminal para tests/API/locust):
```bash
locust -f locustfile.py --host https://demoqa.com
```

#

# Registro de Bugs

Os bugs identificados durante a execução dos testes ou durante a análise da aplicação são registrados no próprio repositório do GitHub.

Eles podem ser visualizados e acompanhados através da aba "Issues", onde são documentados com descrição do problema, passos para reprodução, evidências e informações do ambiente. 

https://github.com/brunohl03/Automa-o-Playwright/issues

#


# Integração Contínua (CI)

O projeto possui integração contínua utilizando GitHub "Actions".

O workflow está definido no arquivo: .github/workflows/CI.yml

https://github.com/brunohl03/Automa-o-Playwright/actions

#



Desenvolvido por Bruno Lima.