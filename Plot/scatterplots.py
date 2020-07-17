import matplotlib.pyplot as plt
import numpy as np

dados_x = np.random.rand(1, 50)
dados_y = np.random.rand(1, 50)

plt.scatter(dados_x, dados_y)

plt.savefig('scatterplot.png')