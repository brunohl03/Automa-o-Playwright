from playwright.sync_api import expect
from utils.data_generator import primeiro_nome, sobrenome, email, idade, salario, departamento
from utils.data_generator import gerar_dados

#  Cenário: pesquisar dados na tabela
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def pesquisar_tabela(page):
    page.get_by_role("textbox", name="Type to search").fill("cierra")

def validar_dados_tabela(page):
    expect(page.get_by_role("cell", name="Cierra", exact=True)).to_be_visible()
 
 #  Cenário: excluir dados da tabela
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def excluir_dados_tabela(page):
    page.locator("#delete-record-1 > svg > path").click()

def validar_exclusao_tabela(page):
    expect(page.get_by_role("cell", name="Cierra", exact=True)).not_to_be_visible()


#  Cenário: editar dados da tabela
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def button_edit(page):
    page.locator("#edit-record-1 > svg").click()

def editar_cierra(page):
    page.get_by_role("textbox", name="First Name").fill(primeiro_nome)
    page.get_by_role("textbox", name="Last Name").fill(sobrenome)
    page.get_by_role("textbox", name="name@example.com").fill(email)
    page.get_by_role("textbox", name="Age").fill(idade)
    page.get_by_role("textbox", name="Salary").fill(salario)
    page.get_by_role("textbox", name="Department").fill(departamento)

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def validar_edit(page):
    expect(page.get_by_role("cell", name=primeiro_nome, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=sobrenome, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=email, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=idade, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=departamento, exact=True)).to_be_visible()

#   Cenário: add pessoa na tabela
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def clicar_add(page):
    page.get_by_role("button", name="Add").click()

def adicionar_um_usuario(page):
    page.get_by_role("textbox", name="First Name").fill(primeiro_nome)
    page.get_by_role("textbox", name="Last Name").fill(sobrenome)
    page.get_by_role("textbox", name="name@example.com").fill(email)
    page.get_by_role("textbox", name="Age").fill(idade)
    page.get_by_role("textbox", name="Salary").fill(salario)
    page.get_by_role("textbox", name="Department").fill(departamento)

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def validar_adicionar_um_usuario(page):
    expect(page.get_by_role("cell", name=primeiro_nome, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=sobrenome, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=email, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=idade, exact=True)).to_be_visible()
    expect(page.get_by_role("cell", name=departamento, exact=True)).to_be_visible()


#  Cenário: validar botão next
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def clicar_add(page):
    page.get_by_role("button", name="Add").click()

def add_novo_usuario(page):
    user = gerar_dados()
    page.get_by_role("textbox", name="First Name").fill(user["primeiro_nome"])
    page.get_by_role("textbox", name="Last Name").fill(user["sobrenome"])
    page.get_by_role("textbox", name="name@example.com").fill(user["email"])
    page.get_by_role("textbox", name="Age").fill(user["idade"])
    page.get_by_role("textbox", name="Salary").fill(user["salario"])
    page.get_by_role("textbox", name="Department").fill(user["departamento"])

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def clicar_next(page):
    page.get_by_text("Next").click()

def validar_numero_linhas(page):
        expect(page.get_by_text("Page 2 of 5")).to_be_visible()


#   Cenário: validar botão previous
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def clicar_add(page):
    page.get_by_role("button", name="Add").click()

def add_novo_usuario(page):
    user = gerar_dados()
    page.get_by_role("textbox", name="First Name").fill(user["primeiro_nome"])
    page.get_by_role("textbox", name="Last Name").fill(user["sobrenome"])
    page.get_by_role("textbox", name="name@example.com").fill(user["email"])
    page.get_by_role("textbox", name="Age").fill(user["idade"])
    page.get_by_role("textbox", name="Salary").fill(user["salario"])
    page.get_by_role("textbox", name="Department").fill(user["departamento"])

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def clicar_last(page):
    page.get_by_role("button", name="Last").click()

def clicar_previous(page):
    page.get_by_role("button", name="Previous").click()

def validar_penultima_pagina(page):
    expect(page.get_by_text("Page 4 of 5")).to_be_visible()


 #  Cenário: validar botão last
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def clicar_add(page):
    page.get_by_role("button", name="Add").click()

def add_novo_usuario(page):
    user = gerar_dados()
    page.get_by_role("textbox", name="First Name").fill(user["primeiro_nome"])
    page.get_by_role("textbox", name="Last Name").fill(user["sobrenome"])
    page.get_by_role("textbox", name="name@example.com").fill(user["email"])
    page.get_by_role("textbox", name="Age").fill(user["idade"])
    page.get_by_role("textbox", name="Salary").fill(user["salario"])
    page.get_by_role("textbox", name="Department").fill(user["departamento"])

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def clicar_last(page):
    page.get_by_role("button", name="Last").click()

def validar_ultima_pagina(page):
    expect(page.get_by_text("Page 5 of 5")).to_be_visible()


 #  Cenário: validar botão first
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def clicar_add(page):
    page.get_by_role("button", name="Add").click()

def add_novo_usuario(page):
    user = gerar_dados()
    page.get_by_role("textbox", name="First Name").fill(user["primeiro_nome"])
    page.get_by_role("textbox", name="Last Name").fill(user["sobrenome"])
    page.get_by_role("textbox", name="name@example.com").fill(user["email"])
    page.get_by_role("textbox", name="Age").fill(user["idade"])
    page.get_by_role("textbox", name="Salary").fill(user["salario"])
    page.get_by_role("textbox", name="Department").fill(user["departamento"])

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def clicar_last(page):
    page.get_by_role("button", name="Last").click()

def clicar_first(page):
    page.get_by_role("button", name="First").click()

def validar_primeira_pagina(page):
    expect(page.get_by_text("Page 1 of 5")).to_be_visible()


#   Cenário: validar show 10
def clicar_elements(page):
    page.get_by_text("Elements").click()

def abrir_web_tables(page):
    page.get_by_text("Web Tables").click()

def clicar_add(page):
    page.get_by_role("button", name="Add").click()

def add_novo_usuario(page):
    user = gerar_dados()
    page.get_by_role("textbox", name="First Name").fill(user["primeiro_nome"])
    page.get_by_role("textbox", name="Last Name").fill(user["sobrenome"])
    page.get_by_role("textbox", name="name@example.com").fill(user["email"])
    page.get_by_role("textbox", name="Age").fill(user["idade"])
    page.get_by_role("textbox", name="Salary").fill(user["salario"])
    page.get_by_role("textbox", name="Department").fill(user["departamento"])

def clicar_submit(page):
    page.get_by_role("button", name="Submit").click()

def selecionar_show_10(page):
    page.get_by_role("combobox").select_option("10")

def selecionar_show_20(page):
    page.get_by_role("combobox").select_option("20")

def selecionar_show_30(page):
    page.get_by_role("combobox").select_option("30")

def selecionar_show_40(page):
    page.get_by_role("combobox").select_option("40")

def selecionar_show_50(page):
    page.get_by_role("combobox").select_option("50")

def validar_linhas_10(page):
    linhas = page.get_by_role("row")
    expect(linhas).to_have_count(11)

def validar_linhas_20(page):
    linhas = page.get_by_role("row")
    expect(linhas).to_have_count(21)

def validar_linhas_30(page):
    linhas = page.get_by_role("row")
    expect(linhas).to_have_count(31)

def validar_linhas_40(page):
    linhas = page.get_by_role("row")
    expect(linhas).to_have_count(41)

def validar_linhas_50(page):
    linhas = page.get_by_role("row")
    expect(linhas).to_have_count(51)