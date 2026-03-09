from pytest_bdd import when, then
from pages.radio_button_page import clicar_elements, abrir_radio_button, selecionar_yes, selecionar_impressive, validar_selecao_yes, validar_selecao_impressive, validar_selecao_no
from utils.helpers import tirar_print


#YES
  
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Radio Button')
def step_abrir_radio_button(page):
    abrir_radio_button(page)
    tirar_print(page, "acessa a seção Radio Button")

@when("seleciona opção Yes")
def step_selecionar_yes(page):
    selecionar_yes(page)
    tirar_print(page, "seleciona opção Yes")

@then("a mensagem You have selected Yes deve aparecer na tela")
def step_validar_selecao_yes(page):
    validar_selecao_yes(page)
    tirar_print(page, "a mensagem You have selected Yes deve aparecer na tela")


#IMPRESSIVE

     
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Radio Button')
def step_abrir_radio_button(page):
    abrir_radio_button(page)
    tirar_print(page, "acessa a seção Radio Button")

@when('seleciona opção impressive')
def step_selecionar_impressive(page):
    selecionar_impressive(page)
    tirar_print(page, "seleciona opção Impressive")

@then('a mensagem You have selected impressive deve aparecer na tela')
def step_validar_selecao_impressive(page):
    validar_selecao_impressive(page)
    tirar_print(page, "a mensagem You have selected Impressive deve aparecer na tela")


#NO


@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Radio Button')
def step_abrir_radio_button(page):
    abrir_radio_button(page)
    tirar_print(page, "acessa a seção Radio Button")


@then('deve ser impedido selecionar a opção no')
def step_validar_selecao_no(page):
    validar_selecao_no(page)
    tirar_print(page, "a mensagem You have selected No deve aparecer na tela")


