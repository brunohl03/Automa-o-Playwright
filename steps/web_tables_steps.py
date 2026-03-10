from pytest_bdd import when, then
from pages.web_tables_page import abrir_web_tables, abrir_web_tables, clicar_elements, excluir_dados_tabela, excluir_dados_tabela, pesquisar_tabela, validar_dados_tabela, validar_exclusao_tabela, validar_exclusao_tabela   
from utils.helpers import tirar_print

#  Cenário: pesquisar dados na tabela
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


#  Cenário: excluir dados da tabela
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when('clicar em delete na linha de cierra')
def step_excluir_dados_tabela(page):
    excluir_dados_tabela(page)

@then('linha de cierra deve ser excluída da tabela')
def step_validar_exclusao_tabela(page):
    validar_exclusao_tabela(page)
