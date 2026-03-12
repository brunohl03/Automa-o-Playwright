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


#   Cenário: Usuário clica no link home dinamico
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_home(page):
    with page.expect_popup() as popup:
        page.locator("#dynamicLink").click()

    return popup.value

def validar_resposta_home(page2):
    expect(page2).to_have_url("https://demoqa.com/")


#   Cenário: Usuário clica no link created
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_created(page):
    page.get_by_role("link", name="Created").click()

def validar_resposta_created(page):
    expect(page.get_by_text("Link has responded with staus", exact=True)).to_be_visible()
    expect(page.get_by_text("201", exact=True)).to_be_visible()
    expect(page.locator("#linkResponse").get_by_text("Created", exact=True)).to_be_visible()