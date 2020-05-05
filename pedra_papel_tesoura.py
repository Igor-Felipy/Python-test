import PySimpleGUI as sg 

class Tela:
    def __init__(self):
        #Layout
        layout = [
            [sg.Radio('Pedra','jogo',key='pedra'),sg.Radio('Papel','jogo',key='papel'),sg.Radio('Tesoura','jogo',key='tesoura')]
        ]
        