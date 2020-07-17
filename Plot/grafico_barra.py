import matplotlib.pyplot as plt

bandas = ['Metalica','Slayer','megadeath']
albuns_estudio = [10, 11, 15]

plt.bar(bandas, albuns_estudio)

plt.savefig('graficos_barras.png')
