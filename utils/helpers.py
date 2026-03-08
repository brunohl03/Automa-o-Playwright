"""
helpers.py

Este arquivo contém funções auxiliares reutilizáveis que facilitam a automação.
Exemplos de funções: clicar em elementos de forma segura, esperar por elementos,
validar textos ou estados da página, manipular dados antes de enviar a formulários.  

Objetivo: reduzir repetição de código, organizar ações comuns e tornar os testes
mais legíveis e fáceis de manter.
"""
import allure

def tirar_print(page, nome):
    print = page.screenshot(path=f"utils/screenshots/{nome}.png")
    allure.attach(print, name=nome, attachment_type=allure.attachment_type.PNG)
