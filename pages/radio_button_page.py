from playwright.sync_api import expect

def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_radio_button(page):
    page.get_by_text("Radio Button").click()

def selecionar_yes(page):
    page.get_by_role("radio", name="Yes").check()

def selecionar_impressive(page):
    page.get_by_role("radio", name="Impressive").check()

def validar_selecao_yes(page):
    expect(page.get_by_text("You have selected Yes")).to_be_visible()

def validar_selecao_impressive(page):
    expect(page.get_by_text("You have selected Impressive")).to_be_visible()

def validar_selecao_no(page):
    expect(page.get_by_role("radio", name="No")).to_be_disabled()

