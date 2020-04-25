class computador:
    def __init__(self, m, r, v):
        self.marca = m
        self.memoria_ram = r
        self.placa_video = v
    

    def Ligar(self):
        print('Estou ligando')

    def Desligar(self):
        print('Estou desligando')

    def Exibir_config(self):
        print(self.marca, self.memoria_ram, self.placa_video)

computador1 = computador('positivo','4gb','GT1030')
computador2 = computador('Asus','16gb','RTX2060super')
computador3 = computador('Alienware','64','sliRTX2080super')

computador1.Exibir_config()
computador2.Exibir_config()
computador3.Exibir_config()
