# Requisitos – Aba Elements (DemoQA)

## Introdução
Este documento descreve os requisitos funcionais e não funcionais da aba Elements do sistema DemoQA. O objetivo é detalhar os comportamentos esperados da aplicação, servindo como base para desenvolvimento e automação de testes.

## Escopo
A aba Elements contempla funcionalidades relacionadas à interação com componentes básicos de interface, incluindo:

- Formulários (Text Box)
- Checkboxes
- Radio Buttons
- Botões
- Links
- Upload e Download de arquivos




## Requisitos Funcionais (RF)

### Formulários (Text Box)

**RF01 – Preenchimento de formulário**  
O sistema deve permitir ao usuário inserir nome completo, e-mail, endereço atual e endereço permanente.

**RF02 – Validação de e-mail**  
O sistema deve validar se o e-mail informado possui formato válido.

**RF03 – Submissão do formulário**  
O sistema deve permitir o envio dos dados após o preenchimento dos campos obrigatórios.

**RF04 – Exibição dos dados enviados**  
O sistema deve exibir os dados submetidos após o envio do formulário.

---

### Checkboxes

**RF05 – Seleção de checkbox**  
O sistema deve permitir selecionar e desmarcar opções de checkbox.

---

### Radio Buttons

**RF06 – Seleção de radio button**  
O sistema deve permitir a seleção de apenas uma opção por vez entre as disponíveis.

---

### Botões

**RF07 – Interação com botões**  
O sistema deve responder corretamente às seguintes ações:
- Clique simples  
- Duplo clique  
- Clique com botão direito  

---

### Upload e Download de arquivos

**RF08 – Upload de arquivo**  
O sistema deve permitir o envio de arquivos a partir do sistema local do usuário.

**RF09 – Download de arquivo**  
O sistema deve permitir o download de arquivos disponíveis na interface.

---

### Links

**RF10 – Exibição de links**  
O sistema deve exibir links interativos na seção de Links.

**RF11 – Navegação via link válido**  
O sistema deve permitir a navegação para uma nova página ao clicar em um link válido.

**RF12 – Abertura de link em nova aba**  
O sistema deve abrir o link em uma nova aba ou janela do navegador, quando aplicável.

**RF13 – Validação de resposta HTTP (link válido)**  
O sistema deve retornar status HTTP de sucesso (200) ao acessar links válidos.

**RF14 – Validação de links inválidos**  
O sistema deve retornar códigos de erro apropriados para links inválidos, incluindo:
- 400 – Bad Request  
- 401 – Unauthorized  
- 403 – Forbidden  
- 404 – Not Found  

**RF15 – Exibição de mensagem de status**  
O sistema deve exibir uma mensagem informando o status da requisição após a interação com o link.

**RF16 – Comportamento sem redirecionamento**  
O sistema deve exibir o resultado da requisição sem necessariamente redirecionar o usuário para outra página, quando aplicável.




## Requisitos Não Funcionais (RNF)

**RNF01 – Tempo de resposta**  
As ações do sistema devem ser executadas em até 3 segundos.

**RNF02 – Compatibilidade**  
O sistema deve ser compatível com os navegadores:
- Chromium  
- Firefox  
- WebKit  

**RNF03 – Usabilidade**  
A interface deve ser clara, intuitiva e de fácil utilização.

**RNF04 – Confiabilidade**  
O sistema não deve perder os dados após a submissão do formulário.

**RNF05 – Testabilidade**  
Os elementos da interface devem possuir identificadores únicos (ID, name, data-testid ou equivalentes) para facilitar a automação de testes.

**RNF06 – Performance**  
A página deve ser carregada completamente em até 5 segundos.

**RNF07 – Tempo de resposta de requisições HTTP**  
As requisições HTTP disparadas pelos links devem retornar em até 3 segundos.

**RNF08 – Consistência de mensagens**  
As mensagens exibidas devem refletir corretamente o status retornado pela requisição.

**RNF09 – Interceptação de requisições**  
As requisições associadas aos links devem ser passíveis de interceptação para validação em testes automatizados.

## Considerações Finais
Este documento serve como base para a criação de cenários de teste e automação utilizando ferramentas como Playwright.  
Os requisitos aqui descritos podem ser refinados conforme a evolução do sistema ou necessidade de cobertura de testes mais detalhada.