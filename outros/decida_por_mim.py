from  random import choice

r = ['Claro','por que não?','Sim','impossivel dizer não!','ta maluco?','Não!','com certeza não!','nem pense!','42','A vida é sua, você escolhe cara!']

while True:
    pergunta = input('Me diga sua duvida e eu te ajudarei a decidir: ')
    print(choice(r))

    f = input('quer perguntar denovo? [S/N] ')
    if f.upper == 'S':
        print('OK')
        continue
    elif f.upper() == 'N':
        print('Então tchau!')
        break
    else:
        print('ERROOOO!!!!!!')
        continue