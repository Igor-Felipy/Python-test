import matplotlib.pyplot as plt

bandas = ['Metalica','Slayer','megadeath']
albuns_estudio = [10, 11, 15]

plt.bar(bandas, albuns_estudio, color='#404040')
plt.title("Albuns de Estúdio")
plt.xlabel("Banda", fontsize=15)
plt.ylabel("Quantidade de albuns", fontsize=15)

plt.savefig('barras_custom.png')
