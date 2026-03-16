from pytest_bdd import when, then
from pages.dynamic_proprieties import clicar_elements, abrir_dynamic_properties, validar_botao_habilitado
from utils.helpers import tirar_print


#   Cenário: Botão fica habilitado após 5s
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção dynamic proprieties')
def step_abrir_dynamic_properties(page):
    abrir_dynamic_properties(page)
    tirar_print(page, "acessa a seção dynamic proprieties")

@then('o botão deve ficar habilitado após 5s')
def step_validar_botao_habilitado(page):
    validar_botao_habilitado(page)
    tirar_print(page, "o botão deve ficar habilitado após 5s")



#   Cenário: Botão muda de cor após 5s
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção dynamic proprieties')
def step_abrir_dynamic_properties(page):
    abrir_dynamic_properties(page)
    tirar_print(page, "acessa a seção dynamic proprieties")

@then('o botão deve mudar de cor após 5s')
def step_validar_botao_habilitado(page):
    validar_botao_habilitado(page)
    tirar_print(page, "o botão deve mudar de cor após 5s")



#   Cenário: Botão fica visivel após 5s
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção dynamic proprieties')
def step_abrir_dynamic_properties(page):
    abrir_dynamic_properties(page)
    tirar_print(page, "acessa a seção dynamic proprieties")
    
@then('o botão deve ficar visivel após 5s')
def step_validar_botao_habilitado(page):
    validar_botao_habilitado(page)
    tirar_print(page, "o botão deve ficar visivel após 5s")    
