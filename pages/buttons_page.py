from playwright.sync_api import expect

#   Cenário: Usuario clica nos botões
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_buttons(page):
    page.get_by_text("Buttons").click()

def click_me(page):
    page.get_by_role("button", name="Click Me", exact=True).click()

def right_click_me(page):
    page.get_by_role("button", name="Right Click Me").click(button="right")    

def double_click_me(page):
    page.get_by_role("button", name="Double Click Me").dblclick()

def validar_mensagens_buttons(page):
    expect(page.get_by_text("You have done a double click")).to_be_visible()
    expect(page.get_by_text("You have done a right click")).to_be_visible()
    expect(page.get_by_text("You have done a dynamic click")).to_be_visible()
    