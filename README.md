# atividades_Flask_API
Código com exemplo de API para gestão de atividades de pessoas.

* Python
* Flask
* SQLAlchemy
* SQLite
* Flask-HTTPAuth

Para executar o código siga os seguintes passos:

1 - Faça o clone do repositório:</br>
$ git clone https://github.com/matt-tavares/atividades_Flask_API.git

2 - Execute o seguinte comando para instalar as dependências:</br>
$ pip install -r requirements.txt

3 - Execute o arquivo models.py para que seja criado a banco de dados SQLite

4 - Execute o arquivo utils.py para que seja adicionado o usuário ao banco de dados (isso é necessário para a autenticação)

5 - Execute o arquivo "run.py"

Ao fazer requisições POST, PUT ou DELETE será necessario usar o método de autenticação basic auth.</br>
username: matheus</br>
password: 123
