from pytest_bdd import when, then
from pages.broken_links_page import abrir_buttons, clicar_elements, clicar_valid_link, validar_broken_image, validar_broken_image, validar_broken_link, validar_broken_status, validar_link_status, validar_valid_image, validar_valid_link, clicar_broken_link
from utils.helpers import tirar_print

#   Cenário: validar valid image
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção Broken Links - Images')
def step_abrir_buttons(page):
    abrir_buttons(page)
    tirar_print(page, "acessa a seção Broken Links - Images")

@then('a imagem valida deve ser carregada corretamente')
def step_validar_valid_image(page):
    validar_valid_image(page)
    tirar_print(page, "Então a imagem valida deve ser carregada corretamente.")



#   Cenário: validar broken image
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção Broken Links - Images')
def step_abrir_buttons(page):
    abrir_buttons(page)
    tirar_print(page, "acessa a seção Broken Links - Images")

@then('a imagem invalida deve estar quebrada e não ser exibida corretamente.')
def step_validar_broken_image(page):
    validar_broken_image(page)
    tirar_print(page, "a imagem invalida deve estar quebrada e não ser exibida corretamente")


#   Cenário: validar valid link
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção Broken Links - Images')
def step_abrir_buttons(page):
    abrir_buttons(page)
    tirar_print(page, "acessa a seção Broken Links - Images")

@when('clica no link válido')
def step_clicar_valid_link(page):
    validar_link_status(page)
    clicar_valid_link(page)
    tirar_print(page, "clica no link válido")

@then('a página vinculada ao link válido deve ser carregada corretamente')
def step_validar_valid_link(page):
    validar_valid_link(page)
    tirar_print(page, "a página vinculada ao link válido deve ser carregada corretamente")


#   Cenário: validar broken link
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção Broken Links - Images')
def step_abrir_buttons(page):
    abrir_buttons(page)
    tirar_print(page, "acessa a seção Broken Links - Images")

@when('clica no link invalido')
def step_clicar_broken_link(page):
    validar_broken_status(page)
    clicar_broken_link(page)
    tirar_print(page, "clica no link invalido")

@then('a página vinculada ao link invalido deve exibir uma mensagem de erro ou não ser carregada corretamente')
def step_validar_broken_link(page):
    validar_broken_link(page)
    tirar_print(page, "a página vinculada ao link invalido deve exibir uma mensagem de erro ou não ser carregada corretamente")
