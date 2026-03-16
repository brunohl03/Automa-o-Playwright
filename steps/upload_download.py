from pytest_bdd import when, then
from pages.upload_download_page import clicar_download, abrir_upload_download, clicar_upload, validar_download, clicar_elements, validar_upload
from utils.helpers import tirar_print

#   Cenário: fazer download de arquivo
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção upload and download')
def step_abrir_upload_download(page):
    abrir_upload_download(page)
    tirar_print(page, "acessa a seção upload and download")

@when('clica em download')
def step_clicar_download(page):
    clicar_download(page)
    tirar_print(page, "clica em download")

@then('deve ser feito o download do arquivo')
def step_validar_download(page):
    validar_download(page)
    tirar_print(page, "deve ser feito o download do arquivo")


#   Cenário: fazer upload de arquivo
@when('ele clica na opção Elements')
def step_clicar_elements(page):
    clicar_elements(page)
    tirar_print(page, "ele clica na opção Elements")

@when('acessa a seção upload and download')
def step_abrir_upload_download(page):
    abrir_upload_download(page)
    tirar_print(page, "acessa a seção upload and download")

@when('clica em upload')
def step_clicar_upload(page):
    clicar_upload(page)
    tirar_print(page, "clica em upload")

@then('deve ser feito o upload do arquivo')
def step_validar_upload(page):
    validar_upload(page)
    tirar_print(page, "deve ser feito o upload do arquivo")


