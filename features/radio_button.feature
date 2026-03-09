# language: pt
Funcionalidade: interagir com elementos

  Cenário: Usuario seleciona opção 'yes' de radio button
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Radio Button
    E seleciona opção Yes
    Então a mensagem You have selected Yes deve aparecer na tela

Cenário: Usuario seleciona opção 'impressive' de radio button
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Radio Button
    E seleciona opção impressive
    Então a mensagem You have selected impressive deve aparecer na tela

Cenário: Usuario seleciona opção 'no' de radio button
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Radio Button
    Então deve ser impedido selecionar a opção no