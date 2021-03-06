# -*- coding: utf-8 -*-

# This code is supporting material for the book
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho
# published by PACKT Publishing
#
# It is made available under the MIT License

import numpy as np
import inspect
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

data = load_iris()

features = data['data']
feature_names = data['feature_names']
target = data['target']

pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
print inspect.getmembers(enumerate(pairs))
for i, (p0, p1) in enumerate(pairs):
    print p0, p1
    print i
    plt.subplot(2, 3, i + 1)
    for t, marker, c in zip(range(3), ">ox", "rgb"):
        plt.scatter(features[target == t, p0], features[
                    target == t, p1], marker=marker, c=c)
        
    #plt.legend(['%s' % data['target_names'][0], '%s' % data['target_names'][1], '%s' % data['target_names'][2]], loc = 'upper left')
    plt.xlabel(feature_names[p0])
    plt.ylabel(feature_names[p1])
    plt.xticks([])
    plt.yticks([])
plt.show()
