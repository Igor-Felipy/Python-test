from random import randint

print('Bem-vindo ao simulador de dados para jogos')
while True:
    lados = int(input('Entre com o valor de lados do seu dado: '))
    qtd = int(input('Quantos dados voce vai jogar? '))
    rol = 0
    for i in range(0, qtd):
        rol = rol + randint(1, lados)

    bonus = input('Você tem algum bonûs??  [S/N] ')
    if bonus.upper() == 'S':
        bo = int(input('coloque o seu bonûs: '))
        rol = rol + bo
    elif bonus.upper() == 'N':
        print('OK!')
    else:
        print('erro!!!')
        continue

    print(rol)
    while True:
        reiniciar = input('Continuar? [S/N] ')
        if reiniciar.upper() == 'S':
            break
        else:
            continue