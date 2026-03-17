from playwright.sync_api import expect
from utils.data_generator import primeiro_nome, email, endereco, pais

def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_text_box(page):
    page.get_by_text("Text Box").click()

def preencher_formulario(page):
    page.get_by_role("textbox", name="Full Name").fill(primeiro_nome)
    page.get_by_role("textbox", name="name@example.com").fill(email)
    page.get_by_role("textbox", name="Current Address").fill(endereco)
    page.locator("#permanentAddress").fill(pais)

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def validar_dados(page):
    expect(page.get_by_text("Name:" + primeiro_nome)).to_be_visible()
    expect(page.get_by_text("Email:" + email)).to_be_visible()
    expect(page.get_by_text("Current Address :" + endereco)).to_be_visible()
    expect(page.get_by_text("Permananent Address :" + pais)).to_be_visible()