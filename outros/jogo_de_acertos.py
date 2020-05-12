from random import randint
n = randint(1, 9)

u = int(input('entre com um numero e descubra se acertou: '))
 
if n == u:
    print('Você acertou!')
else:
    if n < u:
        print('Numero chutado alto demais')
    else:
        print('Numero chutado pequeno demais')
