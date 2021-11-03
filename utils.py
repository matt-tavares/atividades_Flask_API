from models import Pessoas, Usuarios

# Insere dados na tabela pessoa
def insere_Pessoas():
    pessoa = Pessoas(nome='José', idade=25)
    print(pessoa)
    pessoa.save()

# consulta dados da tabela pessoa
def consulta_Pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='José').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_Pessoa():
    pessoa = Pessoas.query.filter_by(nome='José').first()
    pessoa.idade = 22
    pessoa.save()

# Exclui dados da tabela pessoa
def exclui_Pessoa():
    pessoa = Pessoas.query.filter_by(nome='Matheus').first()
    pessoa.delete()

def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__=='__main__':
    insere_usuario("matheus", "123")
    # insere_Pessoas()
    # altera_Pessoa()
    #exclui_Pessoa()
    #consulta_Pessoas()