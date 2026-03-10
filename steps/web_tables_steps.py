from pytest_bdd import when, then
from pages.web_tables_page import abrir_web_tables, abrir_web_tables, button_edit, clicar_elements, clicar_submit, editar_cierra, excluir_dados_tabela, excluir_dados_tabela, pesquisar_tabela, validar_dados_tabela, validar_edit, validar_exclusao_tabela, validar_exclusao_tabela   
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
    tirar_print(page, "pesquisa por cierra")

@then ('somente cierra deve aparecer na tabela')
def step_validar_dados_tabela(page):
    validar_dados_tabela(page) 
    tirar_print(page, "somente cierra deve aparecer na tabela")


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
    tirar_print(page, "clicar em delete na linha de cierra")

@then('linha de cierra deve ser excluída da tabela')
def step_validar_exclusao_tabela(page):
    validar_exclusao_tabela(page)
    tirar_print(page, "linha de cierra deve ser excluída da tabela")


#  Cenário: editar dados da tabela
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when('clicar em edit na linha de cierra')
def step_button_edit(page):
    button_edit(page)
    tirar_print(page, "clicar em edit na linha de cierra")

@when('editar os dados')
def step_editar_cierra(page):
    editar_cierra(page)
    tirar_print(page, "editar os dados")

@when('clicar em submit')
def step_clicar_submit(page):
    clicar_submit(page)
    tirar_print(page, "clicar em submit")

@then('linha de cierra deve ser editada na tabela')
def step_validar_edit(page):
    validar_edit(page)
    tirar_print(page, "linha de cierra deve ser editada na tabela")