# language: pt
Funcionalidade: interagir com elementos

  Cenário: pesquisar dados na tabela
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E pesquisa por cierra
    Então somente cierra deve aparecer na tabela

  Cenário: excluir dados da tabela
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E clicar em delete na linha de cierra
    Então linha de cierra deve ser excluída da tabela

  Cenário: editar dados da tabela
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E clicar em edit na linha de cierra
    E editar os dados
    E clicar em submit
    Então linha de cierra deve ser editada na tabela

  Cenário: add pessoa na tabela
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E clicar em add
    E preencher os dados
    E clicar em submit
    Então novos dados devem ser adicionados na tabela

  Cenário: validar botão next
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E clicar no botão next
    Então deve ser exibida a próxima página da tabela

 Cenário: validar botão previous
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E clicar no botão last
    E clicar no botão previous
    Então deve ser exibida a penultima página da tabela

 Cenário: validar botão last
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E clicar no botão last
    Então deve ser exibida a última página da tabela

 Cenário: validar botão first
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E clicar no botão first
    Então deve ser exibida a primeira página da tabela


Cenário: validar show 10
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E selecionar Show 10 no dropdown
    Então deve conter somente 10 pessoas na tabela

Cenário: validar show 20
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E selecionar Show 20 no dropdown
    Então deve conter somente 20 pessoas na tabela

Cenário: validar show 30
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E selecionar Show 30 no dropdown
    Então deve conter somente 30 pessoas na tabela

Cenário: validar show 40
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E selecionar Show 40 no dropdown
    Então deve conter somente 40 pessoas na tabela

Cenário: validar show 50
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção web tables
    E add 47 pessoas na tabela
    E selecionar Show 50 no dropdown
    Então deve conter somente 50 pessoas na tabela


