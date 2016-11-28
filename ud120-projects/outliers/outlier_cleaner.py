#!/usr/bin/python
import numpy as np

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    list_size = len(ages)

    cleaned_data = []

    errors = []

    ### Calculate errors

    for i in range(list_size):
        error = abs(net_worths[i] - predictions[i])
        errors.append(error)

    ## Remove the highest 9 errors

    for i in range(9):
        index_rm = errors.index(max(errors))
        
        ages = np.delete(ages, index_rm)
        predictions = np.delete(predictions, index_rm)
        net_worths = np.delete(net_worths, index_rm)
        errors.pop(index_rm)

    ### Build cleaned_data

    new_list_size = len(ages)
    
    for i in range(new_list_size):
        temp = (ages[i], net_worths[i], errors[i])
        cleaned_data.append(temp)


    return cleaned_data

