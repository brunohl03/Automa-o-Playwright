from playwright.sync_api import expect
from config.settings import EMAIL_USUARIO, FIRST_NAME, LAST_NAME, IDADE, SALARIO, DEPARTAMENTO

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


#  Cenário: editar dados da tabela
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def button_edit(page):
    page.locator("#edit-record-1 > svg").click()

def editar_cierra(page):
    page.get_by_role("textbox", name="First Name").fill(FIRST_NAME)
    page.get_by_role("textbox", name="Last Name").fill(LAST_NAME)
    page.get_by_role("textbox", name="name@example.com").fill(EMAIL_USUARIO)
    page.get_by_role("textbox", name="Age").fill(IDADE)
    page.get_by_role("textbox", name="Salary").fill(SALARIO)
    page.get_by_role("textbox", name="Department").fill(DEPARTAMENTO)

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def validar_edit(page):
    expect(page.get_by_role("cell", name=FIRST_NAME, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=LAST_NAME, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=EMAIL_USUARIO, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=IDADE, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=DEPARTAMENTO, exact=True)).to_be_visible()

#   Cenário: add pessoa na tabela
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def clicar_add(page):
    page.get_by_role("button", name="Add").click()

def add_novo_usuario(page):
    page.get_by_role("textbox", name="First Name").fill(FIRST_NAME)
    page.get_by_role("textbox", name="Last Name").fill(LAST_NAME)
    page.get_by_role("textbox", name="name@example.com").fill(EMAIL_USUARIO)
    page.get_by_role("textbox", name="Age").fill(IDADE)
    page.get_by_role("textbox", name="Salary").fill(SALARIO)
    page.get_by_role("textbox", name="Department").fill(DEPARTAMENTO)

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def validar_add_novo_usuario(page):
    expect(page.get_by_role("cell", name=FIRST_NAME, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=LAST_NAME, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=EMAIL_USUARIO, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=IDADE, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=DEPARTAMENTO, exact=True)).to_be_visible()