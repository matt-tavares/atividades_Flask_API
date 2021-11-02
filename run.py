from flask import Flask, request
from flask_restful import Resource, Api
from models import Pessoas, Atividades

app = Flask(__name__)
api = Api(app)

class Pessoa(Resource):
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
    def get(self):
        pessoas = Pessoas.query.all()
        response = [{"id": i.id, "nome": i.nome, "idade": i.idade} for i in pessoas]

        return response, 200

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

class ListaAtividade(Resource):
    def get(self):
        atividades = Atividades.query.all()
        response = [{"id": i.id, "nome": i.nome, "pessoa": i.pessoa.nome} for i in atividades]
        return response

    def post(self):
        dados = request.json
        pessoa = Pessoas.query.filter_by(nome=dados['pessoa']).first()
        atividade = Atividades(nome=dados['nome'], pessoa=pessoa)
        atividade.save()
        code = 200
        response = {
            "id": atividade.id,
            "nome": atividade.nome,
            "pessoa": atividade.pessoa.nome
        }
        return response, code


api.add_resource(Pessoa, '/pessoa/<string:nome>')
api.add_resource(ListaPessoas, '/pessoas')
api.add_resource(ListaAtividade, '/atividades')

if __name__=='__main__':
    app.run(debug=True)