'''def doubleNum():
    def receiveNum(num):
        double = num*2

    return receiveNum()


b = doubleNum()
print(b.receiveNum(5))'''
'''
def criaObjeto():
    class pessoa:
        pass
    
    return pessoa

pessoa1 = criaObjeto()

pessoa2 = criaObjeto()


pessoa1.nome = 'igor'
pessoa2.nome = 'felipy'

print(pessoa1.nome)
print(pessoa2.nome)'''

def fabricarPessoa(nome, sobrenome):
    class pessoa:
        pass
    b = pessoa
    pessoa.nome = nome
    pessoa.sobrenome = sobrenome

    return b

pessoaA = fabricarPessoa('Igor', 'França')
pessoaB = fabricarPessoa('Felipy', 'lopes')

print(pessoaA)
print(pessoaB)