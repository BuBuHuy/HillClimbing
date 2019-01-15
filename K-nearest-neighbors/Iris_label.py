# http://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
import numpy as np
from sklearn import datasets
from scipy.spatial import distance
import math
def dis(x,y):
	x2 = np.sum(x*x)
	y2 = np.sum(y*y)

	return x2+y2 - 2*x.dot(y)
iris = datasets.load_iris()
iris_x =iris.data
iris_y=iris.target
test = [7.02,3.16,4.6,1.3]
test = np.array(test)
k_min = 10000
label =1
#cdist(XA, XB, 'euclidean')
for i in range(len(iris_x)):
    t= dis(iris_x[i],test)
    if t < k_min :
        k_min = t
        label = iris_y[i]
print iris.target_names[label]
print k_min