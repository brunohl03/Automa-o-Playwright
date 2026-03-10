from pytest_bdd import when, then
from pages.web_tables_page import abrir_web_tables, abrir_web_tables, clicar_elements, pesquisar_tabela, validar_dados_tabela   
from utils.helpers import tirar_print


@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('pesquisa por cierra')
def step_pesquisar_tabela(page):
    pesquisar_tabela(page)

@then ('somente cierra deve aparecer na tabela')
def step_validar_dados_tabela(page):
    validar_dados_tabela(page) 