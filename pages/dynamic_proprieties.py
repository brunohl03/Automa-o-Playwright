from playwright.sync_api import expect

#   Cenário: Botão fica habilitado após 5s
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_dynamic_properties(page):
    page.get_by_text("Dynamic Properties").click()

def validar_botao_habilitado(page):
    expect(page.get_by_role("button", name="Will enable 5 seconds")).to_be_enabled(timeout=6000)


    
#   Cenário: Botão muda de cor após 5s
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_dynamic_properties(page):
    page.get_by_text("Dynamic Properties").click()

def validar_botao_habilitado(page):
    expect(page.get_by_role("button", name="Color Change")).to_have_class("mt-4 text-danger btn btn-primary", timeout=6000)


#   Cenário: Botão fica visivel após 5s
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_dynamic_properties(page):
    page.get_by_text("Dynamic Properties").click()

def validar_botao_habilitado(page):
    expect(page.get_by_role("button", name="Visible After 5 Seconds")).to_be_visible(timeout=6000)