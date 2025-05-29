from minisom import MiniSom
from sklearn.preprocessing import MinMaxScaler

def treinar_som(X):
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    som = MiniSom(x=7, y=7, input_len=2, sigma=1.0, learning_rate=0.5)
    som.random_weights_init(X_scaled)
    som.train_random(data=X_scaled, num_iteration=200)
    
    return som, X_scaled
