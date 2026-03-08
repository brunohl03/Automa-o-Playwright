from pytest_bdd import when, then
from pages.check_box_pages import clicar_elements, abrir_check_box, expandir_home, validar_check_box
from utils.helpers import tirar_print

@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    

@when('acessa a seção Check Box')
def step_abrir_check_box(page):
    abrir_check_box(page)
    tirar_print(page, "acessa a seção Check Box")

@when("clica na pasta e subpastas em Home")
def step_expandir_home(page):
    expandir_home(page)
    tirar_print(page, "clica na pasta e subpastas em Home")

@then("os dados preenchidos devem aparecer na tela")
def step_validar_check_box(page):
    validar_check_box(page)
    tirar_print(page, "os dados preenchidos devem aparecer na tela")

