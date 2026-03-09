from playwright.sync_api import expect

def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_check_box(page):
    page.get_by_text("Check Box").click()

def expandir_home(page):    
    page.locator(".rc-tree-switcher").click()
    page.get_by_role("checkbox", name="Select Desktop").click()
    page.get_by_role("checkbox", name="Select Documents").click()
    page.get_by_role("checkbox", name="Select Downloads").click()

def validar_check_box(page):
    expect(page.get_by_text("You have selected :", exact=True)).to_be_visible()
    expect(page.get_by_text("desktop", exact=True)).to_be_visible()
    expect(page.get_by_text("notes", exact=True)).to_be_visible()
    expect(page.get_by_text("commands", exact=True)).to_be_visible()
    expect(page.get_by_text("documents", exact=True)).to_be_visible()
    expect(page.get_by_text("workspace", exact=True)).to_be_visible()
    expect(page.get_by_text("office", exact=True)).to_be_visible()
    expect(page.get_by_text("react", exact=True)).to_be_visible()
    expect(page.get_by_text("angular", exact=True)).to_be_visible()
    expect(page.get_by_text("veu", exact=True)).to_be_visible()
    expect(page.get_by_text("public", exact=True)).to_be_visible()
    expect(page.get_by_text("private", exact=True)).to_be_visible()
    expect(page.get_by_text("classified", exact=True)).to_be_visible()
    expect(page.get_by_text("general", exact=True)).to_be_visible()
    expect(page.get_by_text("downloads", exact=True)).to_be_visible()
    expect(page.get_by_text("wordFile", exact=True)).to_be_visible()
    expect(page.get_by_text("excelFile", exact=True)).to_be_visible()
    expect(page.get_by_text("home", exact=True)).to_be_visible()
