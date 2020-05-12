from random import randint
import PySimpleGUI as sg
print('Bem-vindo ao jogo chute um numero!')
class game:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Digite o numero maior a ser jogado'),sg.Input(key='qtd')],
            [sg.Text('Chute um numero:'),sg.Input(key='c')],
            [sg.Button('chute')],
            [sg.Output()]
        ]
        #janela
        self.janela = sg.Window('Jogo de Chute').layout(layout)

    #extração de dados
    def iniciar(self):
        while True:
            self.Button, self.Values = self.janela.Read()
            qtd = self.values['qtd']
            r = randint(0, qtd)
            while True:
                c = self.values['c']
                if c == r:
                    print('Você acertou!')
                    break
                elif c < r:
                    print('Chute um numero maior!')
                elif c > r:
                    print('Chute um numero menor!')
                else:
                    continue

jogo = game()
jogo.iniciar()