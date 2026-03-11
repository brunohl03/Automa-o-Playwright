from playwright.sync_api import expect

#  Cenário: Usuário clica no link home
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_home(page):
    with page.expect_popup() as popup:
        page.locator("#simpleLink").click()

    return popup.value

def validar_resposta_home(page2):
    expect(page2).to_have_url("https://demoqa.com/")