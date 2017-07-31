import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

data_set = {'he' : [[1,2], [2,3], [3,1]], 'she' : [[6,5], [7,7], [8,6]]}
new_features = [5,7]


def k_nearest_neighbours(data, predict, k = 3) :
    if k >= len(data):
        warnings.warn("You are a Idiot, Did you just give heigher K than the data set ??")
    #Store the distance between our target and learned data
    distance = []
    
    # Now calculate the euclidean_distance for each
    for gender in data:
        for features in data[gender]:
            euclidean_distance = np.linalg.norm(np.array(features) - np.array(predict))
            distance.append([euclidean_distance, gender])
    
    #Take the closest one after sorting 
    votes = [i[1] for i  in sorted(distance)[:k]]
    return Counter(votes).most_common(1)[0][0]

print k_nearest_neighbours(data_set, new_features, k=1)   


# Testing this on plot 
# for i in data_set:
#     for features in data_set[i]:
#         plt.scatter(features[0], features[1], s=100)

# plt.scatter(new_features[0], new_features[1], s = 200)        
# plt.show()
