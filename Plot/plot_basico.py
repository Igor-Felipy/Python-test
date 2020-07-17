import matplotlib.pyplot as plt 

numeros = [1, 2, 3, 4, 5]
quadrados = [numero **2 for numero in numeros]

plt.plot(numeros, quadrados)

plt.savefig('plot_basico_1.png')
