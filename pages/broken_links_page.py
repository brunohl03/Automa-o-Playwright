from playwright.sync_api import expect


#   Cenário: validar valid image
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_buttons(page):
    page.get_by_text("Broken Links - Images").click()

def clicar_broken_links(page):
    page.locator("img").nth(1).click()


#   Cenário: validar broken image
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_buttons(page):
    page.get_by_text("Broken Links - Images").click()

def clicar_broken_links(page):
    page.locator("img").nth(2).click()
