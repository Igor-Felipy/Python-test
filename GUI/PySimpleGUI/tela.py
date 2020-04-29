import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        #Layout
        layout = [
            [sg.Text('nome',size=(5,0)),sg.Input(size=(15,0),key='nome')],
            [sg.Text('idade',size=(5,0)),sg.Input(size=(15,0),key='idade')],
            [sg.Text('Quais provedores de e-mail Você aceita?')],
            [sg.Checkbox('Gmail',key='gmail'),sg.Checkbox('Outlook',key='outlook'),sg.Checkbox('Yahoo!',key='yahoo')],
            [sg.Text('Aceita cartões?')],
            [sg.Radio('Sim','cartoes',key='aceitaCartao'),sg.Radio('não','cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',key=('slider'))],
            [sg.Button('Enviar Dados')],
            [sg.Output(size=(30,10))]
        ]
        #Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
       

    def Iniciar(self):
        while True:
             #Extrair os dados da tela
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade = self.values['slider']
            print('nome: {}'.format(nome))
            print('idade: {}'.format(idade))
            print('aceita gmail: {}'.format(aceita_gmail))
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'aceita cartão: {aceita_cartao}')
            print(f'Não aceita cartão: {nao_aceita_cartao}')
            print(f'Velocidade: {velocidade}')

tela = TelaPython()
tela.Iniciar()
