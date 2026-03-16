# language: pt
Funcionalidade: interagir com elementos

  Cenário: fazer download de arquivo
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção upload and download
    E clica em download
    Então deve ser feito o download do arquivo


  Cenário: fazer upload de arquivo
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção upload and download
    E clica em upload
    Então deve ser feito o upload do arquivo