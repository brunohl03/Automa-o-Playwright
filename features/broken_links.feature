# language: pt
Funcionalidade: interagir com elementos

  Cenário: validar valid image
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Broken Links - Images
    Então a imagem valida deve ser carregada corretamente.

  Cenário: validar broken image
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Broken Links - Images
    Então a imagem invalida deve estar quebrada e não ser exibida corretamente.

  Cenário: validar valid link
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Broken Links - Images
    E clica no link válido
    Então a página vinculada ao link válido deve ser carregada corretamente.

  Cenário: validar broken link
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E clica no link invalido
    Então a página vinculada ao link invalido deve exibir uma mensagem de erro ou não ser carregada corretamente.