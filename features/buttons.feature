# language: pt
Funcionalidade: interagir com elementos

  Cenário: Usuario clica nos botões
    Dado que o usuário acessa a página inicial
    Quando ele clica na opção Elements
    E acessa a seção Buttons
    E clica no botão Click Me
    E clica no botão Right Click Me
    E clica no botão Double Click Me
    Então os botões devem responder às ações de clique, clique direito e clique duplo, respectivamente.