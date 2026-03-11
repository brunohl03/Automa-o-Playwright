from pytest_bdd import when, then
from pages.links_page import abrir_links, clicar_elements, clicar_home, validar_resposta_home
from utils.helpers import tirar_print

#  Cenário: Usuário clica no link home
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link Home")
def step_clicar_home(page, context):
    context.page2 = clicar_home(page)
    tirar_print(page, "clica no link Home")

@then("o usuário deve ser redirecionado para a página inicial")
def step_validar_resposta_home(context):
    validar_resposta_home(context.page2)
    tirar_print(context.page2, "o usuário deve ser redirecionado para a página inicial")