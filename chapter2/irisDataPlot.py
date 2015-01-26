# -*- coding: utf-8 -*-

'''
Created on 2015/01/27

@author: fumio
'''


from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()

features = data['data']
feature_names = data['feature_names']
target = data['target']
target_names = data['target_names']
labels = target_names[target]

for t,marker,c in zip(xrange(3), ">ox", "rgb"):
    plt.scatter(features[target == t,0],
                features[target == t,1],
                marker = marker,
                c = c)
    
plt.show()