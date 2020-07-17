import matplotlib.pyplot as plt
import numpy as np

dados_x = np.random.rand(1, 50)
dados_y = np.random.rand(1, 50)
tamanhos = np.random.rand(200, 1000)

plt.scatter(dados_x, dados_y, color = 'orange', s=500, alpha=0.3)

plt.savefig('scatter_custom.png')