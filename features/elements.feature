# language: pt


Funcionalidade: Seção Elements do DemoQA
  Como usuário do site DemoQA
  Quero interagir com os componentes da seção Elements
  Para validar seus comportamentos

  Cenário: Acessar Elements e preencher formulário Text Box
    Dado que o usuário acessa a página "https://demoqa.com/"
    Quando ele clica na opção "Elements"
    E acessa a seção "Text Box"
    E preenche todos os campos obrigatórios
    E clica no botão "Submit"
    Então os dados preenchidos devem ser exibidos na tela

