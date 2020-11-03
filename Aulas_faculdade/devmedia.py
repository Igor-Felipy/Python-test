"""Faça um algoritmo para ler um número que é um código de usuário.

Caso este código seja diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a mensagem "Usuário inválido!" e o sistema será encerrado.

Caso o código seja correto, deve ser lido outro valor que é a senha.

Se a senha estiver correta (a certa é 9999), deve ser exibida a mensagem "Acesso permitido".

Se a senha estiver incorreta deve ser exibida a mensagem "Senha incorreta", e também uma mensagem com as seguintes opções:

1 - tentar novamente
0 - encerrar sistema"""

def password():
    word = int(input("Digite a senha: "))    
    if word == 9999:
        return True
    else:
        return False

def user():
    word = int(input("Digite o codigo de usuario: "))
    if word == 1234:
        return True
    else:
        return False

def main():
    while True:
        login = user()
        if login == True:
            passw = password()
            if passw == True:
                print("Acesso permitido")
            else:
                print("Acesso negado")
                print("1 - tentar novamente")
                print("0 - encerrar sistema")
                end = input("")
                if end == 0:
                    break
                else:
                    continue
        else:
            print("Usuario invalido!")
            break

main()