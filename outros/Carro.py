class carro:
    def __init__(self, c, m):
        self.cor = c
        self.velocidade = 0
        self.marca = m
        self.ligado = False
    

    def ligar(self):
        if self.ligado == True:
            print('Já esta ligado')
        else:
            print('ligando...')
            self.ligado = True
    
    def desligar(self):
        if self.ligado == True:
            self.ligado = False
            print('Desligado...')
        else:
            print('Já está desligado!')
    
    def acelerar(self):
        self.velocidade += 5
    
    def desacelerar(self):
        self.velocidade -= 5
    
    def freiar(self):
        self.velocidade = 0
    
    def velocimetro(self):
        print(self.velocidade)
    
    def status_geral(self):
        print(self.cor, self.marca, self.ligado, self.velocidade)

carro1 = carro('Vermelho','renault')
carro2 = carro('preto','ferrari')
carro3 = carro('amarelo','fiat')

carro1.status_geral()
carro1.ligar()
carro1.acelerar()
carro1.acelerar()
carro1.status_geral()

carro2.status_geral()
carro2.ligar()
carro2.status_geral()
