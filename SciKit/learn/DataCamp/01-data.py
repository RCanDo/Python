#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Loading Your Data Set
subtitle:
version: 1.0
type: tutorial
keywords: [ML, scikit-learn]
description: |
    not only copy
remarks:
todo:
sources:
    - title: Python Machine Learning: Scikit-Learn Tutorial
      chapter: Loading Your Data Set
      link: https://www.datacamp.com/community/tutorials/machine-learning-python
      date: 2019
      authors:
          - fullname: Karlijn Willems
      usage: |
          not only copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: False     # if the file is intended to be run in a terminal
    name: 01-data.py
    path: d:/ROBOCZY/Python/SciKit/learn/DataCamp/
    date: 2019-12-28
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""

#%%
cd d:/ROBOCZY/Python/SciKit/learn/DataCamp/

#%%
"""
data repositories:
http://archive.ics.uci.edu/ml/datasets.php
https://www.kaggle.com/
https://www.kdnuggets.com/datasets/index.html
"""

#%%
from sklearn import datasets

digits = datasets.load_digits()
type(digits)  # sklearn.utils.Bunch
dir(digits)
print(digits)
print(digits['DESCR'])
digits.data
type(digits.data)  # numpy.ndarray
digits.data.size   # 115008
digits.data.shape  # (1797, 64)

#%% importing data directly from remote
import pandas as pd
# loading training set .tra
digits_train = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra", header=None)
digits_train         # 3823 rows x 65 columns
type(digits_train)   # pandas.core.frame.DataFrame

# loading test set .tes
digits_test = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes", header=None)
digits_test         # 1797 rows x 65 columns

#%% EDA for digits
dir(digits)   # ['DESCR', 'data', 'images', 'target', 'target_names']
digits.keys()

print(digits['DESCR'])
digits.data
digits.data.shape    # (1797, 64)
digits.data.min()    # 0.
digits.data.max()    # 16.

digits.images
digits.images.shape  # (1797, 8, 8)
digits.images.min()  # 0.
digits.images.max()  # 16.

(digits.images.reshape(1797, 64) == digits.data).all()  # True

digits.target
digits.target.shape  # 1797
digits.target.min()  # 0
digits.target.max()  # 9

digits.target_names  # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#%% Visualize Your Data Images With matplotlib
import matplotlib.pyplot as plt

# 8 x 8 grid of pictures
def plot_page(page=0):
    fig = plt.figure(figsize=(6, 6))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=.05, wspace=.05)
    for i in range(64):
        ax = fig.add_subplot(8, 8, i+1, xticks=[], yticks=[])
        ax.imshow(digits.images[page*64 + i], cmap=plt.cm.binary, interpolation='nearest')
        ax.text(0, 7, str(digits.target[i]))

    plt.show()

#%%
pages = 1797/64  # 28.078125
plot_page(1)

#%% other way
images_labels = list(zip(digits.images, digits.target))
def plot_page2(page=0):
    a = page * 8
    z = a + 8
    for idx, (img, lab) in enumerate(images_labels[a:z]):
        plt.subplot(2, 4, idx+1)
        plt.axis('off')  # don't plot any axes
        plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Training: ' + str(lab))

#%%
plot_page2()

#%%
#%%
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
digits_pca = pca.fit_transform(digits.data)
digits_pca.shape

#%%
"""
Tip: you have used the RandomizedPCA() here because it performs better
when there’s a high number of dimensions.
Try replacing the randomized PCA model or estimator object
with a regular PCA model and see what the difference is.

in scikit 0.2 + RandomizedPCA is depricated
now it is a parameter PCA(..., svd_solver='randomized', ...)
"""
#%%
rpca = PCA(n_components=2, svd_solver='randomized')
digits_rpca = rpca.fit_transform(digits.data)
digits_rpca.shape

#%%
colors = ['black', 'blue', 'purple', 'yellow', 'white', 'red', 'lime', 'cyan', 'orange', 'gray']
for i in range(len(colors)):
    xx = digits_rpca[:, 0][digits.target == i]
    yy = digits_rpca[:, 1][digits.target == i]
    plt.scatter(xx, yy, c=colors[i])
plt.legend(digits.target_names,
           bbox_to_anchor=(1.05, 1),
           loc=2, borderaxespad=0.)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.title("PCA scatter plot")
plt.show()

# add black boarder for each point !!!

#%%
# use t-SNE for this data

#%%
#%%
from sklearn.preprocessing import scale
digits_scaled = scale(digits.data)

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(digits_scaled, digits.target,
                                         test_size=.25, random_state=42)

X_train.shape  # 1347, 64
X_test.shape   # 450, 64

import numpy as np
np.unique(Y_train)

#%%
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=10, init='k-means++', random_state=42, n_init=10)
kmeans_fit = kmeans.fit(X_train)

#%% how the cluster centers look like:
fig = plt.figure(figsize=(8, 3))
fig.suptitle('Cluster center images', fontsize=14, fontweight='bold')
for i in range(10):
    ax = fig.add_subplot(2, 5, 1+i)
    ax.imshow(kmeans_fit.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)
    plt.axis('off')
plt.show()

#%% comparing predictions with labels
Y_pred = kmeans_fit.predict(X_test)     #!
for p, l in zip(Y_pred, Y_test):
    print(p, l)

import pandas as pd
digdf = pd.DataFrame({'pred': Y_pred, 'label': Y_test})
sum(digdf['pred'] - digdf['label'] != 0)  # 396

#%%
# https://scikit-learn.org/stable/modules/generated/sklearn.manifold.Isomap.html#sklearn.manifold.Isomap
# https://scikit-learn.org/stable/modules/manifold.html#isomap
from sklearn.manifold import Isomap

X_iso = Isomap(n_neighbors=10).fit_transform(X_train)

# Compute cluster centers and predict cluster index for each sample
clusters = kmeans_fit.fit_predict(X_train)     #!

# Create a plot with subplots in a grid of 1X2
fig, ax = plt.subplots(1, 2, figsize=(8, 4))

# Adjust layout
fig.suptitle('Predicted Versus Training Labels', fontsize=14, fontweight='bold')
fig.subplots_adjust(top=0.85)

# Add scatterplots to the subplots
ax[0].scatter(X_iso[:, 0], X_iso[:, 1], c=clusters)
ax[0].set_title('Predicted Training Labels')
ax[1].scatter(X_iso[:, 0], X_iso[:, 1], c=Y_train)
ax[1].set_title('Actual Training Labels')

# Show the plots
plt.show()

#%% model evaluation
'%d' % kmeans_fit.inertia_  #???

"""
 https://scikit-learn.org/stable/modules/clustering.html#clustering-evaluation
"""
from sklearn import metrics
metrics.confusion_matrix(Y_test, Y_pred)

"""
 https://scikit-learn.org/stable/modules/clustering.html#homogeneity-completeness-and-v-measure
homogeneity: each cluster contains only members of a single class.
completeness: all members of a given class are assigned to the same cluster.
V-measure: their harmonic mean = 2*h*c/(h+c)
"""
'%.3f' % metrics.homogeneity_score(Y_test, Y_pred)
'%.3f' % metrics.completeness_score(Y_test, Y_pred)
# they are mutually symmetric
metrics.homogeneity_score(Y_test, Y_pred) - metrics.completeness_score(Y_pred, Y_test)
# only numeric error but we cannot use ==
#
'%.3f' % metrics.v_measure_score(Y_test, Y_pred)
# is symmetric
'%.3f' % metrics.v_measure_score(Y_pred, Y_test)
#
# all together
metrics.homogeneity_completeness_v_measure(Y_test, Y_pred)
'%.3f, %.3f, %.3f' % metrics.homogeneity_completeness_v_measure(Y_test, Y_pred)

"""
Adjusted Rand Index
https://scikit-learn.org/stable/modules/clustering.html#adjusted-rand-index
...pairs...
"""
'%.3f' % metrics.adjusted_rand_score(Y_test, Y_pred)  # symmetric
'%.3f' % metrics.adjusted_rand_score(Y_pred, Y_test)  # symmetric

"""
Adjusted Mutual Information (AMI)
https://scikit-learn.org/stable/modules/clustering.html#mutual-information-based-scores
"""
'%.3f' % metrics.adjusted_mutual_info_score(Y_test, Y_pred) # symmetric
'%.3f' % metrics.adjusted_mutual_info_score(Y_pred, Y_test)

"""
Silhouette Coefficient
https://scikit-learn.org/stable/modules/clustering.html#silhouette-coefficient
(*) = the mean distance between a sample and all other points...
a = (*) in the same class.
b = (*) in the next nearest cluster.
The Silhouette Coefficient s for a single sample is then given as:
    s = (b-a)/max(a, b)
"""
'%.3f' % metrics.silhouette_score(X_test, Y_pred, metric='euclidean')


#%%
#%% Trying Out Another Model: Support Vector Machines
#%%

#%%
from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test, images_train, images_test = \
    train_test_split(digits.data, digits.target, digits.images,
                     test_size=.25, random_state=42)

X_train.shape  # 1347, 64
X_test.shape   # 450, 64

import numpy as np
np.unique(Y_train)

#%%
from sklearn import svm
svc = svm.SVC(gamma=.001, C=100, kernel="linear")
svc.fit(X_train, Y_train)

#%% grid search for the best meta-parameters
X_train, X_test, Y_train, Y_test, images_train, images_test = \
    train_test_split(digits.data, digits.target, digits.images,
                     test_size=.5, random_state=0)

from sklearn.model_selection import GridSearchCV
parameter_sets = [
        {'C':[1, 10, 100, 1000], 'kernel':['linear']},
        {'C':[1, 10, 100, 1000], 'kernel':['rbf'], 'gamma':[.001, .0001]},
    ]

grid_search_cv = GridSearchCV(estimator=svm.SVC(),
                              param_grid=parameter_sets,
                              n_jobs=-1)

grid_search_cv.fit(X_train, Y_train)

grid_search_cv.best_score_
grid_search_cv.best_estimator_.C
grid_search_cv.best_estimator_.kernel
grid_search_cv.best_estimator_.gamma

grid_search_cv.score(X_test, Y_test)   # .9911

#%% Support Vector Classifier
X_train, X_test, Y_train, Y_test, images_train, images_test = \
    train_test_split(digits.data, digits.target, digits.images,
                     test_size=.25, random_state=42)

svc = svm.SVC(gamma=.001, kernel='rbf', C=10)
svc_fit = svc.fit(X_train, Y_train)
svc_fit.score(X_test, Y_test)   # .9911

#%%
Y_hat = svc.predict(X_test)
svcpd = pd.DataFrame({'pred':Y_hat, 'true':Y_test})
svcpd
sum(svcpd['pred'] != svcpd['true'])  # 4

#%%
img_and_pred = list(zip(images_test, Y_hat))

for i, (img, pred) in enumerate(img_and_pred[:4]):
    plt.subplot(1, 4, i + 1)
    plt.axis('off')
    plt.imshow(img, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Predicted: ' + str(pred))

plt.show()

#%% the biggest question: how does this model perform?
from sklearn import metrics
print(metrics.classification_report(Y_test, Y_hat))
metrics.confusion_matrix(Y_test, Y_hat)

#%%
from sklearn.manifold import Isomap
X_iso = Isomap(n_neighbors=10).fit_transform(X_train)
Y_hat_train = svc.predict(X_train)

fig, ax = plt.subplots(1, 2, figsize=(8, 4))
fig.subplots_adjust(top=.85)
ax[0].scatter(X_iso[:, 0], X_iso[:, 1], c=Y_hat_train)
ax[0].set_title('Predicted labels')
ax[1].scatter(X_iso[:, 0], X_iso[:, 1], c=Y_train)
ax[1].set_title('True labels')
fig.suptitle('Predicted vs true labels', fontsize=14, fontweight='bold')
plt.show()

#%%


