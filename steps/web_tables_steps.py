from pytest_bdd import when, then
from config.settings import DEPARTAMENTO
from pages.web_tables_page import clicar_first, selecionar_show_10, clicar_first, selecionar_show_10, selecionar_show_20, selecionar_show_30, selecionar_show_30, selecionar_show_40, selecionar_show_50, validar_linhas_10, validar_linhas_20, validar_linhas_30, validar_linhas_40, validar_linhas_50, validar_primeira_pagina, validar_ultima_pagina, abrir_web_tables, abrir_web_tables, add_novo_usuario, button_edit, clicar_add, clicar_elements, clicar_submit, editar_cierra, excluir_dados_tabela, excluir_dados_tabela, pesquisar_tabela, validar_add_novo_usuario, validar_dados_tabela, validar_edit, validar_exclusao_tabela, validar_exclusao_tabela, validar_numero_linhas, validar_numero_linhas, clicar_last, clicar_next, clicar_previous, validar_penultima_pagina     
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


#  Cenário: add pessoa na tabela
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when('clicar em add')
def step_clicar_add(page):
    clicar_add(page)
    tirar_print(page, "clicar em add")

@when('preencher os dados')
def step_add_novo_usuario(page):
    add_novo_usuario(page)
    tirar_print(page, "preencher os dados")

@when('clicar em submit')
def step_clicar_submit(page):
    clicar_submit(page)
    tirar_print(page, "clicar em submit")

@then('novos dados devem ser adicionados na tabela')
def step_validar_add_novo_usuario(page):
    validar_add_novo_usuario(page)
    tirar_print(page, "novos dados devem ser adicionados na tabela")

    
#   Cenário: validar botão next
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('clicar no botão next')
def step_clicar_next(page):
    page.get_by_role("button", name="Next").click()
    tirar_print(page, "clicar no botão next")

@then ('deve ser exibida a próxima página da tabela')
def step_validar_proxima_pagina(page):
    validar_numero_linhas(page)
    tirar_print(page, "deve ser exibida a próxima página da tabela")


#  Cenário: validar botão previous
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('clicar no botão last')
def step_clicar_last(page):
    clicar_last(page)
    tirar_print(page, "clicar no botão last")

@when ('clicar no botão previous')
def step_clicar_previous(page):
    clicar_previous(page)
    tirar_print(page, "clicar no botão previous")

@then ('deve ser exibida a penultima página da tabela')
def step_validar_penultima_pagina(page):
    validar_penultima_pagina(page)
    tirar_print(page, "deve ser exibida a penultima página da tabela")


#  Cenário: validar botão last
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('clicar no botão last')
def step_clicar_last(page):
    clicar_last(page)
    tirar_print(page, "clicar no botão last")

@then ('deve ser exibida a última página da tabela')
def step_validar_ultima_pagina(page):
    validar_ultima_pagina(page)
    tirar_print(page, "deve ser exibida a última página da tabela")


#   Cenário: validar botão first
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('clicar no botão last depois first')
def step_clicar_last_depois_first(page):
    clicar_last(page)
    clicar_first(page)

@then ('deve ser exibida a primeira página da tabela')
def step_validar_primeira_pagina(page):
    validar_primeira_pagina(page)
    tirar_print(page, "deve ser exibida a primeira página da tabela")


#   Cenário: validar show 10
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('selecionar Show 10 no dropdown')
def step_selecionar_show_10(page):
    selecionar_show_20(page)
    tirar_print(page, "selecionar Show 20 no dropdown")
    selecionar_show_10(page)
    tirar_print(page, "selecionar Show 10 no dropdown")

@then ('deve conter somente 10 pessoas na tabela')
def step_validar_show_10(page):
    validar_linhas_10(page)
    tirar_print(page, "deve conter somente 10 pessoas na tabela")


#   Cenário: validar show 20
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('selecionar Show 20 no dropdown')
def step_selecionar_show_20(page):
    selecionar_show_20(page)
    tirar_print(page, "selecionar Show 20 no dropdown")


@then ('deve conter somente 20 pessoas na tabela')
def step_validar_show_20(page):
    validar_linhas_20(page)
    tirar_print(page, "deve conter somente 20 pessoas na tabela")


#   Cenário: validar show 30
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('selecionar Show 30 no dropdown')
def step_selecionar_show_30(page):
    selecionar_show_30(page)
    tirar_print(page, "selecionar Show 30 no dropdown")


@then ('deve conter somente 30 pessoas na tabela')
def step_validar_show_30(page):
    validar_linhas_30(page)
    tirar_print(page, "deve conter somente 30 pessoas na tabela")


#   Cenário: validar show 40
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('selecionar Show 40 no dropdown')
def step_selecionar_show_40(page):
    selecionar_show_40(page)
    tirar_print(page, "selecionar Show 40 no dropdown")


@then ('deve conter somente 40 pessoas na tabela')
def step_validar_show_40(page):
    validar_linhas_40(page)
    tirar_print(page, "deve conter somente 40 pessoas na tabela")


#   Cenário: validar show 50
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção web tables')
def step_abrir_web_tables(page):
    abrir_web_tables(page)
    tirar_print(page, "acessa a seção web tables")

@when ('add 47 pessoas na tabela')
def step_add_47_pessoas(page):
    for _ in range(47):
        clicar_add(page)
        add_novo_usuario(page)
        clicar_submit(page)

    tirar_print(page, "add 47 pessoas na tabela")

@when ('selecionar Show 50 no dropdown')
def step_selecionar_show_50(page):
    selecionar_show_50(page)
    tirar_print(page, "selecionar Show 50 no dropdown")


@then ('deve conter somente 50 pessoas na tabela')
def step_validar_show_50(page):
    validar_linhas_50(page)
    tirar_print(page, "deve conter somente 50 pessoas na tabela")