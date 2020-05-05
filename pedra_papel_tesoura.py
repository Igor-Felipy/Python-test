import PySimpleGUI as sg 
from random import choice
c = ['pedra','papel','tesoura']
class Tela:
    def __init__(self):
        #Layout
        layout = [
            [sg.Radio('Pedra','jogo',key='pedra',size=(5,0)),sg.Radio('Papel','jogo',key='papel',size=(5,0)),sg.Radio('Tesoura','jogo',key='tesoura',size=(5,0))],
            [sg.Text('',size=(5,0)),sg.Button('jogar',size=(5,0)),sg.Text('',size=(5,0))],
            [sg.Output(size=(15,5))]
        ]

        #Janela
        self.janela = sg.Window("Jogo").layout(layout)

    
    def iniciar(self):
        while True:
            #extração
            self.button, self.Values = self.janela.Read()
            pd = self.Values['pedra']
            pp = self.Values['papel']
            ts = self.Values['tesoura']
            a = choice(c)
            print('='*15)
            print('A maquina escolheu {}'.format(a))
            print('='*15)
            if pd:
                print('='*15)
                print('voce escolheu Pedra')
                print('='*15)
                if a = 'pedra':
                    print('empate')
                elif a = 'tesoura':
                    print('você venceu')
                else:
                    print('Você perdeu!')
            elif pp:
                print('='*15)
                print('voce escolheu Papel')
                print('='*15)
                if a = 'papel':
                    print('empate')
                elif a = 'pedra':
                    print('Voce venceu')
                else:
                    print('voce perdeu')
            elif ts:
                print('='*15)
                print('voce escolheu tesoura')
                print('='*15)
                if a = 'tesoura':
                    print('empate')
                elif a = 'papel':
                    print('Voce venceu')
                else:
                    print('Voce perdeu')
            else:
                print('erro')