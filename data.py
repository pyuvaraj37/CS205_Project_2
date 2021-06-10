import numpy as np
import matplotlib.pyplot as plt
import string

def Data(path_to_data):

    features = []
    labels = []
    number_of_features = 0
    file = open(path_to_data, 'r')
    for line in file:
        line = repr(line)
        line = line.strip('\'\\n')
        line = line.split()    
        number_of_features = len(line) - 1; 
        labels.append(line[0])
        features.append([float(i) for i in line[1:]])
        
    return features, labels, number_of_features