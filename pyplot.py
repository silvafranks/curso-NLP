import matplotlib.pyplot as plt

# Dados
palavras = [26, 101, 161, 194, 222, 261, 405, 504, 675]
tempo = [0.000000083, 0.000000205, 0.000000167, 0.000000222, 0.000000326, 0.000000225, 0.000000366, 0.000000466, 0.000000645]

# Gráfico de Dispersão
plt.figure(figsize=(10, 5))
plt.scatter(palavras, tempo, color='blue', label='Dispersão')
plt.xlabel('Número de Palavras')
plt.ylabel('Tempo (segundos)')
plt.title('Gráfico de Dispersão')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de Linha
plt.figure(figsize=(10, 5))
plt.plot(palavras, tempo, color='red', marker='o', linestyle='-', linewidth=1, markersize=6, label='Linha')
plt.xlabel('Número de Palavras')
plt.ylabel('Tempo (segundos)')
plt.title('Gráfico de Linha')
plt.legend()
plt.grid(True)
plt.show()