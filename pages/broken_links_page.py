from playwright.sync_api import expect


#   Cenário: validar valid image
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_buttons(page):
    page.get_by_text("Broken Links - Images").click()

def validar_valid_image(page):
    expect(page.locator("img").nth(1)).to_be_visible()



#   Cenário: validar broken image
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_buttons(page):
    page.get_by_text("Broken Links - Images").click()

def validar_broken_image(page):
    expect(page.locator("img").nth(2)).not_to_be_visible()


#   Cenário: validar valid link
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_buttons(page):
    page.get_by_text("Broken Links - Images").click()

def clicar_valid_link(page):
    page.get_by_role("link", name="Click Here for Valid Link").click()

def validar_valid_link(page):
    expect(page).to_have_url("https://demoqa.com/")

def validar_link_status(page):
    link = page.get_by_role("link", name="Click Here for Valid Link")
    url = link.get_attribute("href")
    response = page.request.get(url)
    assert response.status == 200


#   Cenário: validar broken link
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_buttons(page):
    page.get_by_text("Broken Links - Images").click()

def clicar_broken_link(page):
    page.get_by_role("link", name="Click Here for Broken Link").click()

def validar_broken_link(page):
    expect(page).to_have_url("http://the-internet.herokuapp.com/status_codes/500")

def validar_broken_status(page):
    link = page.get_by_role("link", name="Click Here for Broken Link")
    url = link.get_attribute("href")
    response = page.request.get(url)
    assert response.status == 500
