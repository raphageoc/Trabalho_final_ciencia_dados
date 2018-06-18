# -*- coding: utf-8 -*-

import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.cluster import AgglomerativeClustering


arq = open('iris.data', 'r')
dado = []
for i in arq:
	dado.append(str(i).split(',')[0:4])
t=len(dado)

x = np.array(dado[0:t-1])
x = x.astype(float)





clustering = AgglomerativeClustering(linkage='ward', n_clusters=3)
plt.figure(figsize=(10, 4))
clustering.fit(x)
plt.scatter(x[:, 0], x[:, 3], c=clustering.labels_)
plt.axis('equal')
plt.axis('on')
plt.show()
