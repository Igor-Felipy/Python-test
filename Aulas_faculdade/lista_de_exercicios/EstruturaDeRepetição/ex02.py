#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

while True:
    user = str(input('Usuario: '))
    password = str(input('Senha: '))
    if user == password:
        print('Usuario e senha iguais, tente novamente!')
        continue
    else:
        print('OK!')
        break