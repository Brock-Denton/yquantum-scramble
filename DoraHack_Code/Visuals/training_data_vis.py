# visualization of training data (sets of 50 0's and 1's, separated into 3 classes)
# some of the code taken from:
# https://github.com/dorahacksglobal/quantum-randomness-generator/blob/QC-Prediction-Model/classification/RandomNumber_Classification.ipynb

import numpy as np
# import pandas as pd
import matplotlib.pyplot as plt

def load_train_data(filepath):
    # returns np array of the data
    data = []
    with open(filepath, 'r') as f:
        for line in f: # loop through lines in file
            if line.strip(): # skip empty lines
                binary_number, label = line.strip().split()
                data.append(list(int(b) for b in binary_number) + [int(label),])
    return np.array(data)

def main():
    filepath = 'AI_2qubits_training_data.txt'

    data = load_train_data(filepath)

    # print(data.shape) # (6000, 2)
    means1 = np.mean(data[data[:, -1] == 1][:, :-1], 0)
    means2 = np.mean(data[data[:, -1] == 2][:, :-1], 0)
    means3 = np.mean(data[data[:, -1] == 3][:, :-1], 0)

    # plot means of each sample as histograms
    n_bins = 7
    fig, (ax0, ax1, ax2) = plt.subplots(3, 1, sharex=True, tight_layout=True)
    ax0.hist(means1)
    ax1.hist(means2)
    ax2.hist(means3)

    plt.show()

if __name__=='__main__': main()