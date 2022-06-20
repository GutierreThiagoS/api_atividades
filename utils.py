from models import Pessoas, db_session

def insere_pessoas():
    pessoa = Pessoas(nome= "Thiago", idade= 28)
    print(pessoa)
    pessoa.save()

def consulta_pessoas():
    pessoa = Pessoas.query.all()
    print(pessoa)


def altera_pessoa():
    pessoa= Pessoas.query.filter_by(nome="Thiago").first()
    pessoa.idade = 21
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Thiago").first()
    pessoa.delete()

if __name__ == '__main__':
    consulta_pessoas()
    # insere_pessoas()
    #altera_pessoa()
   # exclui_pessoa()
    consulta_pessoas()
