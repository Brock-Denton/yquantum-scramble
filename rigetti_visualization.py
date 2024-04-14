# visualize QRNG output from Rigetti device

import numpy as np
import matplotlib.pyplot as plt

def load_data(filepath):
    # returns np array (1-dim) of data
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            if line.strip():
                data.append(int(line.strip()))
    return np.array(data)

def main():
    filepath = 'rigetti_DIQRNG.txt'
    data = load_data(filepath)
    moving_avg = []
    step = 50
    width = 250
    for i in range(data.shape[0] // step):
        moving_avg.append(np.mean(data[i*step:i*step + width]))
    moving_avg = np.array(moving_avg)
    plt.plot(np.arange(data.shape[0]//step), moving_avg)
    plt.show()

if __name__=='__main__': main()