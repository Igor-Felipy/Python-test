from random import randint
import PySimpleGUI as sg

class GUI:
    def __init__(self):
        #layout
        layout = [
            [sg.Text('Quantidade de lados'),sg.Slider(range = (4,250),default_value=4,orientation='h',key='lados')],
            [sg.Text('Quantidade de dados'),sg.Slider(range = (1,50),default_value=1,orientation = 'h',key='qtd')],
            [sg.Text('Voce tem bonus?'),sg.Radio('Sim','Bonus',key='S'),sg.Radio('Não','Bonus',key='N')],
            [sg.Text('Quantidade de bonus'),sg.Slider(range = (0,200), default_value = 1, orientation = 'h',key='bonus')],
            [sg.Button('Jogar os Dados')],
            [sg.Output(size=(45,10))]
        ]
        #janela
        self.janela = sg.Window("Dados virtuais").layout(layout)

    def iniciar(self):
        #extração de dados
        while True:
            self.button, self.values = self.janela.Read()
            bonus = self.values['bonus']
            lados = self.values['lados']
            qtd = int(self.values['qtd'])
            rol = 0
            b = self.values['S']
            for i in range(0, qtd):
                rol = rol + randint(1, lados)

            if b:
                rol = rol + bonus
            
            print('='*20)
            print(int(rol))
            print('='*20)

tela = GUI()
tela.iniciar()