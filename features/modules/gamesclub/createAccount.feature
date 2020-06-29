 
Funcionalidade: Criar conta
    Criar conta para acessar a plataforma gamesclub

    Contexto: Formulário

    @full
    Esquema do Cenário: Cadastrar conta

        Dado que acessei o site gamesclub
        Quando eu clico no botão criar conta
        E preencho o campo email com "<email>"
        E preencho o campo confirmação de email com "<email>"
        E preencho o campo senha com "<password>"
        E devo clicar em cadastrar
        E preencho o campo nome com "<name>"
        E preencho o campo apelido com "<nickname>"
        E devo clicar no botão proximo
        Então devo visualizar a mensagem de sucesso


        Exemplos: Cadastro de contas
            | email                                 | password                |  name     | nickname     |
            | gamesclub2000@yopmail.com             | teste123                |  teste    | teste1234    |

