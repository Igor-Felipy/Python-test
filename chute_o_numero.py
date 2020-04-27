from random import randint
print('Bem-vindo ao jogo chute um numero!')

while True:
    qtd = int(input('Digite a quantidade de possibilidades: '))
    r = randint(0, qtd)
    while True:
        c = int(input('Chute um numero entre 0 e {}: '.format(qtd)))
        if c == r:
            print('Você acertou!')
            break
        elif c < r:
           print('Chute um numero maior!')
        elif c > r:
            print('Chute um numero menor!')
        else:
            continue
