from validate import leave_one_out_cross_validation

def feature_search_forward_selection(number_of_features, features, labels, empty_feature_set, full_feature_set):
    
    current_set_of_features = empty_feature_set

    best_accuracy_set = []
    best_global_accuracy = 0;
    
    print("Starting feature search...")
    for i in range(1, number_of_features + 1):
        print('The current set is {}'.format(current_set_of_features))
        print('On the {}th level of the search tree'.format(i))
        feature_to_add_at_this_level = []
        best_so_far_accuracy = 0

        for j in range(1, number_of_features + 1):
            if j not in current_set_of_features:
                print("--Considering adding the {} feature".format(j))
                accuracy = leave_one_out_cross_validation(features=features, labels=labels, current_set_of_features=current_set_of_features, feature_to_explore=j, methd='forward')
                print("Adding that feature gives an accuracy of {}".format(accuracy))
                if accuracy > best_so_far_accuracy:
                    best_so_far_accuracy = accuracy
                    feature_to_add_at_this_level = j
                    

        current_set_of_features.append(feature_to_add_at_this_level)
        if best_so_far_accuracy >= best_global_accuracy:
            best_global_accuracy = best_so_far_accuracy
            best_accuracy_set = current_set_of_features.copy()
        print("On level {} i added feature {} to current set".format(i, feature_to_add_at_this_level))
    
    print("Best accuracy was acheived with features {} that has an accuracy of {}".format(best_accuracy_set, best_global_accuracy))


def feature_search_backward_elimination(number_of_features, features, labels, full_feature_set):
    
    current_set_of_features = full_feature_set
    
    print("Starting feature search...")
    for i in range(1, number_of_features + 1):
        print('The current set is {}'.format(current_set_of_features))
        print('On the {}th level of the search tree'.format(i))
        feature_to_remove_at_this_level = []
        worst_so_far_accuracy = 1

        for j in range(1, number_of_features + 1):
            if j in current_set_of_features:
                print("--Considering removing the {} feature".format(j))
                accuracy = leave_one_out_cross_validation(features=features, labels=labels, current_set_of_features=current_set_of_features, feature_to_explore=j, methd='backward')
                print("Removing that feature gives an accuracy of {}".format(accuracy))
                if accuracy < worst_so_far_accuracy:
                    worst_so_far_accuracy = accuracy
                    feature_to_remove_at_this_level = j
        
        current_set_of_features.remove(feature_to_remove_at_this_level)
        print("On level {} i removed feature {} to current set".format(i, feature_to_remove_at_this_level))