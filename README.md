# Deploy de uma aplicação Flask no heroku

## Antes de tudo

- ter python instalado no seu computador veja aqui [faça aqui o download](https://www.python.org/downloads/)

- ter o o cli de comandos do heroku instalado no seu computador [faça aqui o download](https://devcenter.heroku.com/articles/heroku-cli)


Configurando o ambiente testando antes do deploy!

```git clone https://github.com/J0a0Paul0Jp/InvestSys.git```

```python3 -m venv .env```

```source .env/bin/activate``` no **Linux**

```C:\> .env\Scripts\activate.bat```  no **Windows**

```pip install -r requirements.txt```

```export FLASK_APP=app```

```export FLASK_ENV=development```

```flask run```


Tendo tudo funcionando vamos para o deploy \o/
## HEROKU 


Caso você já tenha uma conta criada no heroku pule a o tutorial de criar uma conta!
## Criando uma Conta

Acesse o https://signup.heroku.com/login crie sua conta clicando em [sign-up](https://id.heroku.com/signup/login)

como descrito na imagem abaixo

![img](https://i.imgur.com/Ra0UL7T.png)

## Depois de criado a conta você já pode fazer [login](https://id.heroku.com/login)

Configurando o ambiente para fazer o deploy 

Após já está logado na conta do heroku você devera criar um novo app, a opção fica bem visível na tela inicial de usuário, procure por "new" ou "new create app", escolha o nome para seu projeto e confirme a criação, tendo feito isso, seu projeto vai está pronto pra deploy no heroku 

## Vamos ao deploy!

Abre seu prompt de comando de seu sistema operacional, no Linux é o terminal
navegue ao diretório que se enconta seu projeto em Flask, normalmente você navega usando ```cd direto_do_projeto``` no meu caso faço ```cd InvestSys```
execute os seguintes comandos abaixo!

```heroku login``` -> O comando conecta sua conta do heroku ao seu computador, abra o link que aparece após a execução do comando, normalmente é aberto automaticamente e confirme no botão de login, volte ao terminal, se tudo der certo vai ter a mensagem "Logging in... done
"

Crie um arquivo ```Procfile```: necessário para o heroku conhecer o ponto de partida de nossa Aplicação, então nesse arquivo cole o seguinte comando ```web: flask run --host=0.0.0.0 --port=$PORT```


```git init``` -> comando pra criar um novo repositório

```heroku git:remote -a investsystrader``` -> obs: o "investsystrader" foi o nome que dei ao app no heroku que criei utilizando o "new" nos passos anterioriores, coloque de acordo com o nome do qual você digitou na criação do seu próprio app, o comando dar permissão remota de fazer alterações no app que criamos pra posteriomente serem modificadas

```git add .``` -> adiciona os arquivos de seu projeto ao repositório criado

```git commit -am "subindo minha aplicação no heroku"``` -> confirma as alterações de adição

```git push heroku master``` -> esse é comando para o sucesso, ele vai subir os arquivos de sua máquina de forma remota para o app que você criou no heroku

## Hora da verdade :grinning:!

antes de tudo você deve criar sua variável de ambiente no heroku, você vai ir no app que você criou depois clique em settings, encontre o botão de "Reveal Config Vars", e crie uma variável de ambiente em ```KEY``` defina como ```FLASK_ENV``` no ```VALUE``` dela coloque como ```production```, depois de tudo só confirmar clicando em "ADD"

```heroku app``` -> quando executado esse comando ele vai abrir seu app, já mostrando seu webapp rodando

ou

acesse a url pra ver minha aplicação rodando, de acordo com os passos anteriores
https://investsystrader.herokuapp.com/login
