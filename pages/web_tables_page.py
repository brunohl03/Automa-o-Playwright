from playwright.sync_api import expect
from config.settings import NOME_USUARIO, EMAIL_USUARIO, CURRENT_ADDRESS, PERMANENT_ADDRESS

#  Cenário: pesquisar dados na tabela
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def pesquisar_tabela(page):
    page.get_by_role("textbox", name="Type to search").fill("cierra")

def validar_dados_tabela(page):
    expect(page.get_by_role("cell", name="Cierra", exact=True)).to_be_visible()
 
 #  Cenário: excluir dados da tabela
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def excluir_dados_tabela(page):
    page.locator("#delete-record-1 > svg > path").click()

def validar_exclusao_tabela(page):
    expect(page.get_by_role("cell", name="Cierra", exact=True)).not_to_be_visible()