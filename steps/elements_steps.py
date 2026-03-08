from pytest_bdd import when, then
from pages.elements_page import clicar_elements, abrir_text_box, preencher_formulario, clicar_submit, validar_dados
from utils.helpers import tirar_print

@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção Text Box')
def step_abrir_text_box(page):
    abrir_text_box(page)
    tirar_print(page, "acessa a seção Text Box")

@when("preenche o formulário")
def step_preencher_formulario(page):
    preencher_formulario(page)
    tirar_print(page, "preenche o formulário")

@when('clica no botão Submit')
def step_clicar_submit(page):
    clicar_submit(page)
    tirar_print(page, "clica no botão Submit")

@then("os dados preenchidos devem aparecer na tela")
def step_validar_dados(page):
    validar_dados(page)
    tirar_print(page, "os dados preenchidos devem aparecer na tela")