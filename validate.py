from random import *
import numpy as np
from math import sqrt

def leave_one_out_cross_validation(features, labels, current_set_of_features, feature_to_explore, methd):

    number_correctly_classified = 0; 

    test_set_of_features = current_set_of_features.copy()
    if methd == 'forward':
        test_set_of_features.append(feature_to_explore)
    elif methd == 'backward':
        test_set_of_features.remove(feature_to_explore)


    for i in range(len(labels)):
        
        object_to_classify = (features[i][x - 1] for x in test_set_of_features)
        object_to_classify = list(object_to_classify)
        object_to_classify = np.array(object_to_classify)
        
        label_object_to_classify = labels[i]
        
        nearest_neighbor_distance = float('inf');
        nearest_neighbor_location = float('inf');

        for j in range(len(labels)):
            if j != i:
                #print('Ask if {} is nearest neighbor with {}'.format(i+1, j+1))
                
                neighbor_data = (features[j][x - 1] for x in test_set_of_features)
                neighbor_data = list(neighbor_data)
                neighbor_data = np.array(neighbor_data)
                
            
                # print(object_to_classify)
                # print(neighbor_data)

                distance = sqrt(sum((object_to_classify - neighbor_data)**2))
                if distance < nearest_neighbor_distance:
                    nearest_neighbor_distance = distance
                    nearest_neighbor_location = j
                    nearest_neighbor_label = labels[j]
        
        #print('Object {} is class {}'.format(i+1, label_object_to_classify))
        #print('Its nearest neighboir is {} which is class {}'.format(nearest_neighbor_location + 1, nearest_neighbor_label))
        if label_object_to_classify == nearest_neighbor_label:
            number_correctly_classified+=1
        
    accuracy = number_correctly_classified/len(labels)
    return accuracy