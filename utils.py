from models import Pessoas, Usuarios, db_session

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

def insere_usuario(login, senha):
    usuarios = Usuarios(login=login, senha=senha)
    usuarios.save()

def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    insere_usuario("gutierre1", "1234")
    insere_usuario("thiago1", "4321")
    consulta_todos_usuarios()
    #consulta_pessoas()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
