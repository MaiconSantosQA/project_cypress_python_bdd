 
Funcionalidade: Criar conta
    Criar conta para acessar a plataforma gamesclub

    Contexto: Formulário


      @full  @test
    Esquema do Cenário: Senha invalida

        Dado que acessei o site gamesclub
        Quando eu clico no botão login
        E preencho o campo login com "<email>"
        E preencho o campo senha com "<password>"
        E clico no botão entrar
        Então devo visualizar uma mensagem de erro

        Exemplos: Emails
            | email                                 | password                |
            | gamesclub1@yopmail.com                | test0000                |

     @full
    Esquema do Cenário: Login

        Dado que acessei o site gamesclub
        Quando eu clico no botão login
        E preencho o campo login com "<email>"
        E preencho o campo senha com "<password>"
        E clico no botão entrar
        Então devo logar na plataforma com sucesso

        Exemplos: Emails
            | email                                 | password                |
            | gamesclub12@yopmail.com               | teste123                |

