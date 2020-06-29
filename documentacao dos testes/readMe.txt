Para iniciar os testes execute os seguintes comandos:
1 -  pip install -r requirements.txt
2 -  CD  C:\seu local\GC\GamesClub
3 -  
behave features\modules\gamesclub\createAccount.feature -t=full -D environment=test –k
behave features\modules\gamesclub\login.feature -t=full -D environment=test –k
behave features\modules\gamesclub\confirmEmail.feature -t=full -D environment=test –k

Obs: Os testes são independentes possibilitando a execução sem uma ordem especifica, para a criação da conta é necessario colocar um novo email toda vez que for rodar, o ideal seria excluir a conta com um script direto no banco de dados após finalizar os testes, eu poderia ter colocado emails ramdômicos porem achei mais interessante o usuario colocar direto no .feature para dar liberdade para a pessoa escolher o e-mail desejado.
