import matplotlib.pyplot as plt
import numpy as np

dados = np.random.randn(500)
plt.hist(dados, alpha=0.5, color='purple',edgecolor='black')
plt.show()

plt.savefig('historigrama.png')