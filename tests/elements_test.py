from pytest_bdd import scenarios, when, then
from pages.elements_page import (clicar_elements,abrir_text_box,preencher_formulario,validar_dados,clicar_submit)

scenarios("../features/elements.feature")

@when('ele clica na opção "Elements"')
def step_clicar_elements(page):
    clicar_elements(page)


@when('acessa a seção "Text Box"')
def step_abrir_text_box(page):
    abrir_text_box(page)


@when("preenche todos os campos obrigatórios")
def step_preencher_formulario(page):
    preencher_formulario(page)


@when('clica no botão "Submit"')
def step_clicar_submit(page):
    clicar_submit(page)


@then("os dados preenchidos devem ser exibidos na tela")
def step_validar_dados(page):
    validar_dados(page)