from playwright.sync_api import expect
from config.settings import NOME_USUARIO, EMAIL_USUARIO, CURRENT_ADDRESS, PERMANENT_ADDRESS

def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_text_box(page):
    page.get_by_text("Text Box").click()

def preencher_formulario(page):
    page.get_by_role("textbox", name="Full Name").fill(NOME_USUARIO)
    page.get_by_role("textbox", name="name@example.com").fill(EMAIL_USUARIO)
    page.get_by_role("textbox", name="Current Address").fill(CURRENT_ADDRESS)
    page.locator("#permanentAddress").fill(PERMANENT_ADDRESS)

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def validar_dados(page):
    expect(page.get_by_text("Name:" + NOME_USUARIO)).to_be_visible()
    expect(page.get_by_text("Email:" + EMAIL_USUARIO)).to_be_visible()
    expect(page.get_by_text("Current Address :" + CURRENT_ADDRESS)).to_be_visible()
    expect(page.get_by_text("Permananent Address :" + PERMANENT_ADDRESS)).to_be_visible()