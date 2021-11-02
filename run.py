from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
    # Busca os dados de uma pessoa
    def get(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            code = 200
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade,
            }
        except AttributeError:
            code = 400
            response = {"status": "error", "mensangem": "Pessoa não encontrada"}
        return response, code

    # Altera os dados de uma pessoa
    def put(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        dados = request.json
        try:
            if 'nome' in dados:
                pessoa.nome = dados['nome']
            if 'idade' in dados:
                pessoa.idade = dados['idade']
            pessoa.save()
            code = 200
            response = {
                'id': pessoa.id,
                'nome': pessoa.nome,
                'idade': pessoa.idade,
            }
        except AttributeError:
            code = 400
            response = {"status": "error", "mensangem": "Pessoa não encontrada"}
        return response, code

    # Exclui os dados de pessoa
    def delete(self, nome):
        pessoa = Pessoas.query.filter_by(nome=nome).first()
        try:
            code = 200
            mensagem = '{} exclído(a) com sucesso!'.format(pessoa.nome)
            response = {'status': 'Ok', 'mensagem': mensagem}
            pessoa.delete()
        except AttributeError:
            code = 400
            response = {"status": "error", "mensangem": "Pessoa não encontrada"}
        return response, code

class ListaPessoas(Resource):
    # Busca os dados de todas as pessoas
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id": i.id, "nome": i.nome, "idade": i.idade} for i in pessoas]

        return response, 200

    # Cadastra pessoa
    def post(self):
        dados = request.json
        pessoa = Pessoas(nome=dados['nome'], idade=dados['idade'])
        pessoa.save()
        code = 200
        response = {
            'id': pessoa.id,
            'nome': pessoa.nome,
            'idade': pessoa.idade
        }
        return response, code

class Atividade(Resource):
    # Busca uma atividade pelo id
    def get(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        try:
            code = 200
            response = {
                "id": atividade.id,
                "nome": atividade.nome,
                "pessoa": atividade.pessoa.nome,
                "status": atividade.status
            }
        except AttributeError:
            code = 400
            response = {"status": "error", "menssagem": "Nenhum registro encontrado"}
        return response, code

    # Altera os dados de uma atividade
    def put(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        dados = request.json
        if 'nome' in dados:
            atividade.nome = dados['nome']
        if 'pessoa' in dados:
            atividade.pessoa.nome = dados['pessoa']
        if 'status' in dados:
            atividade.status = dados['status']
        atividade.save()
        code = 200
        response = {
            "id": atividade.id,
            "nome": atividade.nome,
            "pessoa": atividade.pessoa.nome,
            "status": atividade.status
        }
        return response, code

    # Exclui uma atividade
    def delete(self, id):
        atividade = Atividades.query.filter_by(id=id).first()
        try:
            code = 200
            response = {'status': 'Ok', 'mensagem': 'Atividade excluída com sucesso!'}
            atividade.delete()
        except AttributeError:
            code = 400
            response = {"status": "error", "mensangem": "Atividade não encontrada"}
        return response, code

class ListaAtividade(Resource):
    # Busca todas as atividades
    def get(self):
        atividades = Atividades.query.all()
        response = [{"id": i.id, "nome": i.nome, "pessoa": i.pessoa.nome, "status": i.status} for i in atividades]
        return response

    # Cadastra uma atividade
    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], status="pendente", pessoa=pessoa)
        atividade.save()
        code = 200
        response = {
            "id": atividade.id,
            "nome": atividade.nome,
            "status": atividade.status,
            "pessoa": atividade.pessoa.nome
        }
        return response, code

class AtividadePessoa(Resource):
    def get(self, id):
        atividades = Atividades.query.filter_by(pessoa_id=id)
        response = [{"id": i.id, "nome": i.nome, "pessoa": i.pessoa.nome, "status": i.status} for i in atividades]
        return response

api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListaPessoas, '/pessoas')
api.add_resource(Atividade, '/atividade/<string:id>')
api.add_resource(ListaAtividade, '/atividades')
api.add_resource(AtividadePessoa, '/atividade/pessoa/<string:id>')

if __name__=='__main__':
    app.run(debug=True)