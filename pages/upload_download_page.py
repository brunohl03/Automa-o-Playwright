from playwright.sync_api import expect


#   Cenário: fazer download de arquivo
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_upload_download(page):
    page.get_by_text("Upload and download").click()

def clicar_download(page):
   with page.expect_download() as download_info:
        page.get_by_role("button", name="Download").click()
        
   download = download_info.value

def validar_download(download):
    assert download is not None

"""
clicar_download()   
      ↓
Playwright começa a escutar download
      ↓
botão é clicado
      ↓
arquivo começa a baixar
      ↓
Playwright captura o download
      ↓
validar_download()
      ↓
expect confirma que o download existe

"""

#   Cenário: fazer upload de arquivo
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_upload_download(page):
    page.get_by_text("Upload and download").click()

def clicar_upload(page):
    page.locator("#uploadFile").set_input_files("utils/upload_images/wp6726163-isle-of-man-tt-wallpapers.jpg")

def validar_upload(page):
    expect(page.get_by_text("C:\\fakepath\\wp6726163-isle-of-man-tt-wallpapers.jpg")).to_be_visible()

"""
pytest
   ↓
Playwright executa set_input_files
   ↓
procura arquivo no disco
   ↓
Automa-o-Playwright/utils/upload_images/
   ↓
simula seleção do arquivo no input file

"""