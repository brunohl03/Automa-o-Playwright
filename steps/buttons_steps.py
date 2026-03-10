from pytest_bdd import when, then
from pages.buttons_page import clicar_elements, abrir_buttons, click_me, right_click_me, double_click_me, validar_mensagens_buttons
from utils.helpers import tirar_print

#   Cenário: Usuario clica nos botões
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Buttons')
def step_abrir_buttons(page):
    abrir_buttons(page)
    tirar_print(page, "acessa a seção Buttons")

@when ('clica no botão Click Me')
def step_click_me(page):
    click_me(page)
    tirar_print(page, "clica no botão Click Me")

@when ('clica no botão Right Click Me')
def step_right_click_me(page):
    right_click_me(page)

@when ('clica no botão Double Click Me')
def step_double_click_me(page):
    double_click_me(page)
    tirar_print(page, "clica no botão Double Click Me")

@then('os botões devem responder às ações de clique, clique direito e clique duplo, respectivamente.')
def step_validar_mensagens_buttons(page):
    validar_mensagens_buttons(page)