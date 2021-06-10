from data import Data
from search import feature_search_forward_selection, feature_search_backward_elimination
from validate import leave_one_out_cross_validation
import time

def main():
    print("Nearest-Neighbor!")
    
    arg = input("Would you like to use a small or large or real dataset: (1 for small, 2 for large, 3 real data)")
    if (int(arg) == 1):
        arg = int(input("Dataset 10, 19, and 28 avalible: (type the number)"))
        if (arg == 10):
            data = 'test_data/CS205_small_testdata__10.txt'
        elif(arg == 19):
            data = 'test_data/CS205_small_testdata__19.txt'
        elif(arg == 28):
            data = 'test_data/CS205_small_testdata__28.txt'

    elif (int(arg) == 2):
        arg = int(input("Dataset 1, 24, and 28 avalible: (type the number)"))
        if (arg == 1):
            data = 'test_data/CS205_large_testdata__1.txt'
        elif(arg == 24):
            data = 'test_data/CS205_large_testdata__24.txt'
        elif(arg == 28):
            data = 'test_data/CS205_large_testdata__28.txt'
    
    elif (int(arg) == 3):
        arg = int(input("Dataset small 24, and large 43 avalible: (type the number)"))
        if(arg == 24):
            data = 'real_data/CS205_small_testdata__24.txt'
        elif(arg == 43):
            data = 'real_data/CS205_large_testdata__43.txt'
    else:
        exit()
    
    features, labels, number_of_features = Data(data)
    
    samples_size = len(labels)
    print("The Data set {} has {} features, and {} samples".format(arg, number_of_features, samples_size))
    full_feature_set = []
    empty_feature_set = []
    full_feature_set.extend(range(1, number_of_features + 1))

    start_time = time.time()
    feature_search_forward_selection(number_of_features=number_of_features, features=features, labels=labels, empty_feature_set=empty_feature_set, full_feature_set=full_feature_set)
    
    #feature_search_backward_elimination(number_of_features=number_of_features, features=features, labels=labels, full_feature_set=full_feature_set)
    print("Search took %s" % (time.time() - start_time))
    #full_set_accuracy = leave_one_out_cross_validation(features=features, labels=labels, current_set_of_features=full_feature_set, feature_to_explore=0, methd='')
    #print('All the features have an accuracy of {}'.format(full_set_accuracy))

if __name__ == "__main__":
    main()