import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets.samples_generator import make_circles
import matplotlib.pyplot as plt
from itertools import cycle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score
from mpl_toolkits.mplot3d import axes3d, Axes3D





X,_ = make_circles(n_samples=2000, factor=.5,
                                      noise=.05)

# print(X[0])
# print(X[0,0])

ms = AgglomerativeClustering()
ms.fit(X)
labels = ms.labels_


labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)


print("number of estimated clusters : %d" % n_clusters_)

fig = plt.figure(1)
plt.clf()



colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    plt.scatter(X[my_members, 0], X[my_members, 1], c=col)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()

train, test, train_labels, test_labels = train_test_split(X,labels,test_size=0.33,random_state=42)

gnb = BernoulliNB()

model = gnb.fit(train, train_labels)

preds = gnb.predict(test)

print(accuracy_score(test_labels, preds))