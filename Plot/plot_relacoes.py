import matplotlib.pyplot as plt 

numeros = [1, 2, 3, 4, 5]
quadrados = [numero ** 2 for numero in numeros]
cubos = [numero ** 3 for numero in numeros]

plt.plot(numeros, quadrados, color = 'red', linewidth = '5', label = 'quadrados')
plt.plot(numeros, cubos, color = 'green', linewidth = '5', label = 'cubos')

plt.legend()

#label dos eixos
plt.xlabel("Numeros", fontsize=15)
plt.ylabel("Quadrados", fontsize=15)

plt.savefig('plot_relacional.png')