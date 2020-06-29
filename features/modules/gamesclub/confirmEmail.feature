 
Funcionalidade: Criar conta
    Criar conta para acessar a plataforma gamesclub

    Contexto: Formulário

    @full
    Esquema do Cenário: Verificar email de confirmação

        Dado que acessei o site hostmail
        Quando eu preencho o campo email com "<email>"
        E clico no botão acessar email
        Então devo visualizar o email de confirmação
        Então devo clicar em confirmar


        Exemplos: usuarios fakes
            | email                                 |
            | gamesclub12                           |

