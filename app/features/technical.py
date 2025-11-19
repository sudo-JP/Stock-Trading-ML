import numpy as np 


def calculate_rsi(prices: np.array, window: int) -> np.array:
    # Pure vectorized RSI implementation
    deltas = np.diff(prices)
    gains = np.where(deltas > 0, deltas, 0)
    losses = np.where(deltas < 0, -deltas, 0)

    
    return deltas  

def calculate_macd(prices: np.array) -> tuple:
    # MACD, signal line, histogram
    pass

def bollinger_bands(prices: np.array, window: int, num_std: int):
    # Upper, lower bands, middle line
    #pass RSI, MACD, Bollinger bands 
    pass

if __name__ == '__main__': 
    print(calculate_rsi(np.array([10, 12, 11, 13, 12, 14, 13, 15, 14, 16], dtype=float), 3))
