from pytest_bdd import when, then
from pages.links_page import abrir_links, clicar_created, clicar_elements, clicar_home, clicar_moved, clicar_no_content, clicar_unauthorized, validar_resposta_bad_request, validar_resposta_created, validar_resposta_forbidden, validar_resposta_home, validar_resposta_moved, validar_resposta_no_content, clicar_moved, validar_resposta_moved, validar_resposta_bad_request, clicar_bad_request, validar_resposta_not_found, validar_resposta_unauthorized, clicar_forbidden, validar_resposta_forbidden, clicar_not_found, validar_resposta_not_found
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


#   Cenário: Usuário clica no link home dinamico
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link Home dinamico")
def step_clicar_home(page, context):
    context.page2 = clicar_home(page)
    tirar_print(page, "clica no link Home")

@then("o usuário deve ser redirecionado para a página inicial")
def step_validar_resposta_home(context):
    validar_resposta_home(context.page2)
    tirar_print(context.page2, "o usuário deve ser redirecionado para a página inicial")


#   Cenário: Usuário clica no link created
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link Created")
def step_clicar_created(page):
    clicar_created(page)
    tirar_print(page, "clica no link Created")

@then("o usuário deve visualizar Link has responded with staus 201 and status text Created")
def step_validar_resposta_created(page):
    validar_resposta_created(page)
    tirar_print(page, "o usuário deve visualizar Link has responded with staus 201 and status text Created")


#   Cenário: Usuário clica no link no content
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link No Content")
def step_clicar_no_content(page):
    clicar_no_content(page)
    tirar_print(page, "clica no link No Content")

@then("o usuário deve visualizar Link has responded with staus 204 and status text No Content")
def step_validar_resposta_no_content(page):
    validar_resposta_no_content(page)
    tirar_print(page, "o usuário deve visualizar Link has responded with staus 204 and status text No Content")


#   Cenário: Usuário clica no link moved
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link moved")
def step_clicar_moved(page):
    clicar_moved(page)
    tirar_print(page, "clica no link Moved")

@then("o usuário deve visualizar Link has responded with staus 301 and status text Moved Permanently")
def step_validar_resposta_moved(page):
    validar_resposta_moved(page)
    tirar_print(page, "o usuário deve visualizar Link has responded with staus 301 and status text Moved Permanently")


#   Cenário: Usuário clica no link bad request
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link bad request")
def step_clicar_bad_request(page):
    clicar_bad_request(page)
    tirar_print(page, "clica no link Bad Request")

@then("o usuário deve visualizar Link has responded with staus 400 and status text Bad Request")
def step_validar_resposta_bad_request(page):
    validar_resposta_bad_request(page)
    tirar_print(page, "o usuário deve visualizar Link has responded with staus 400 and status text Bad Request")


#   Cenário: Usuário clica no link unauthorized
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link unauthorized")
def step_clicar_unauthorized(page):
    clicar_unauthorized(page)
    tirar_print(page, "clica no link Unauthorized")
    
@then("o usuário deve visualizar Link has responded with staus 401 and status text Unauthorized")
def step_validar_resposta_unauthorized(page):
    validar_resposta_unauthorized(page)
    tirar_print(page, "o usuário deve visualizar Link has responded with staus 401 and status text Unauthorized")


#   Cenário: Usuário clica no link forbidden
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link forbidden")
def step_clicar_forbidden(page):
    clicar_forbidden(page)
    tirar_print(page, "clica no link Forbidden")

@then("o usuário deve visualizar Link has responded with staus 403 and status text Forbidden")
def step_validar_resposta_forbidden(page):
    validar_resposta_forbidden(page)
    tirar_print(page, "o usuário deve visualizar Link has responded with staus 403 and status text Forbidden")


#   Cenário: Usuário clica no link not found
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")
    
@when('acessa a seção Links')
def step_abrir_links(page):
    abrir_links(page)
    tirar_print(page, "acessa a seção Links")

@when("clica no link not found")
def step_clicar_not_found(page):
    clicar_not_found(page)
    tirar_print(page, "clica no link Not Found")

@then("o usuário deve visualizar Link has responded with staus 404 and status text Not Found")
def step_validar_resposta_not_found(page):
    validar_resposta_not_found(page)
    tirar_print(page, "o usuário deve visualizar Link has responded with staus 404 and status text Not Found")
    