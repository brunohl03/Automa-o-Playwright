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
    expect(page.locator("#linkResponse")).to_contain_text("Link has responded with status 201 and status text Created")


#   Cenário: Usuário clica no link no content
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_no_content(page):
    page.get_by_role("link", name="No Content").click()

def validar_resposta_no_content(page):
    expect(page.locator("#linkResponse")).to_contain_text("Link has responded with status 204 and status text No Content")


#   Cenário: Usuário clica no link moved
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_moved(page):
    page.get_by_role("link", name="Moved").click()

def validar_resposta_moved(page):
    expect(page.locator("#linkResponse")).to_contain_text("Link has responded with status 301 and status text Moved Permanently")


#   Cenário: Usuário clica no link bad request
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_bad_request(page):
    page.get_by_role("link", name="Bad Request").click()

def validar_resposta_bad_request(page):
   expect(page.locator("#linkResponse")).to_contain_text("Link has responded with status 400 and status text Bad Request")


#   Cenário: Usuário clica no link unauthorized
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_unauthorized(page):    
    page.get_by_role("link", name="Unauthorized").click()

def validar_resposta_unauthorized(page):    
    expect(page.locator("#linkResponse")).to_contain_text("Link has responded with status 401 and status text Unauthorized")


#   Cenário: Usuário clica no link forbidden
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_forbidden(page):
    page.get_by_role("link", name="Forbidden").click()

def validar_resposta_forbidden(page):
    expect(page.locator("#linkResponse")).to_contain_text("Link has responded with status 403 and status text Forbidden")


#   Cenário: Usuário clica no link not found
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_links(page):
    page.get_by_text("Links", exact=True).click()

def clicar_not_found(page):
    page.get_by_role("link", name="Not Found").click()

def validar_resposta_not_found(page):
    expect(page.locator("#linkResponse")).to_contain_text("Link has responded with status 404 and status text Not Found")
