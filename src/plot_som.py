import matplotlib.pyplot as plt
import numpy as np
import os

def plotar_mapa(som, X_scaled, y):
    width = som._weights.shape[0]
    height = som._weights.shape[1]

    plt.figure(figsize=(10, 10))

    # Frequência de ativações
    frequencies = np.zeros((width, height))
    for x in X_scaled:
        w = som.winner(x)
        frequencies[w[0], w[1]] += 1

    # Heatmap
    plt.pcolor(frequencies.T, cmap='Blues', edgecolors='k', linewidths=1)
    plt.colorbar(label="Número de ativações")

    # Plotar os rótulos
    for i, x in enumerate(X_scaled):
        w = som.winner(x)
        plt.text(w[0] + 0.5, w[1] + 0.5, str(y[i]),
                 ha='center', va='center',
                 bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

    plt.title("Mapa Auto-Organizado (SOM) com Heatmap")
    plt.xticks(np.arange(width + 1))
    plt.yticks(np.arange(height + 1))
    plt.gca().invert_yaxis()
    plt.grid(True)

    os.makedirs("figuras", exist_ok=True)
    plt.savefig("figuras/mapa_resultado.png")
    plt.show()
