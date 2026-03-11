# language: pt
Funcionalidade: interagir com elementos

  Cenário: Usuário clica no link home
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link Home
    Então o usuário deve ser redirecionado para a página inicial

  Cenário: Usuário clica no link home dinamico
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link Home dinamico
    Então o usuário deve ser redirecionado para a página inicial

  Cenário: Usuário clica no link created
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link Created
    Então o usuário deve visualizar Link has responded with staus 201 and status text Created

  Cenário: Usuário clica no link no content
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link No Content
    Então o usuário deve visualizar Link has responded with staus 204 and status text No Content

  Cenário: Usuário clica no link moved
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link moved
    Então o usuário deve visualizar Link has responded with staus 301 and status text Moved Permanently

  Cenário: Usuário clica no link bad request
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link bad request
    Então o usuário deve visualizar Link has responded with staus 400 and status text Bad Request

  Cenário: Usuário clica no link unauthorized
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link unauthorized
    Então o usuário deve visualizar Link has responded with staus 401 and status text Unauthorized

  Cenário: Usuário clica no link forbidden
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link forbidden
    Então o usuário deve visualizar Link has responded with staus 403 and status text Forbidden

  Cenário: Usuário clica no link not found
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Links
    E clica no link not found
    Então o usuário deve visualizar Link has responded with staus 404 and status text Not Found
    



