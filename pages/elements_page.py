from playwright.sync_api import expect

def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_text_box(page):
    page.get_by_text("Text Box").click()

def preencher_formulario(page):
    page.get_by_role("textbox", name="Full Name").fill("Bruno Lima")
    page.get_by_role("textbox", name="name@example.com").fill("bruno.lima@example.com")
    page.get_by_role("textbox", name="Current Address").fill("Rua Exemplo, 123")
    page.locator("#permanentAddress").fill("Rua Exemplo, 456")

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def validar_dados(page):
    expect(page.get_by_text("Name:Bruno Lima")).to_be_visible()
    expect(page.get_by_text("Email:bruno.lima@example.com")).to_be_visible()
    expect(page.get_by_text("Current Address :Rua Exemplo, 123")).to_be_visible()
    expect(page.get_by_text("Permananet Address :Rua Exemplo, 456")).to_be_visible()