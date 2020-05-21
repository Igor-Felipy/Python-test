class Eletronico:
    def __init__(self):
        self.ligado = False
    def ligar(self):
        self.ligado = True
    def desligar(self):
        self.ligado = False
    def esta_ligado(self):
        return self.ligado
    
class TV(Eletronico):
    def __init__(self):
        Eletronico.__init__(self)
        self.volume = 0
    def aumentar_volume(self):
        self.volume = self.volume +1
    def diminuir_volume(self):
        if self.volume > 0:
            self.volume = self.volume -1
    def obter_volume(self):
        return self.volume
    

class iPhone(Eletronico):
    def __init__(self):
        Eletronico.__init__(self)
        self.tocando_musica = False
    def tocar_musica(self):
        self.tocando_musica = True
    def parar_musica(self):
        self.tocando_musica = False
    def tocando_som(self):
        return self.tocando_musica

