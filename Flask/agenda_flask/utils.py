from models import Pessoas

def consulta_um(nome_entrada):
    pessoa = Pessoas.query.filter_by(nome=nome_entrada).first()
    print(pessoa)

def consulta_todos():
    pessoa = Pessoas.query.all()
    print(pessoa)

def inserir_pessoa(nome, idade):
    pessoa = Pessoas(nome=nome, idade=idade)
    pessoa.save()
    print("Ok")

def alterar_dados_pessoa(nome_atual, novo_nome):
    pessoa = Pessoas.query.filter_by(nome=nome_atual).first()
    pessoa.nome = novo_nome
    pessoa.save()

def deletar_pessoa(nome_entrada):
    pessoa = Pessoas.query.filter_by(nome=nome_entrada).first()
    pessoa.delete()

if __name__ == '__main__':
    inserir_pessoa('Oliveira', 23)
    consulta_um('Oliveira')
    consulta_todos()
    alterar_dados_pessoa('Oliveira', 'OLIVER')
    deletar_pessoa('OLIVER')
    consulta_todos()