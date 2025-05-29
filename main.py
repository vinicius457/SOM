from src.gerar_dados import gerar_dados
from src.treinar_som import treinar_som
from src.plot_som import plotar_mapa

X, y = gerar_dados()
som, X_scaled = treinar_som(X)
plotar_mapa(som, X_scaled, y)
