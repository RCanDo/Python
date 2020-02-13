# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:55:06 2019

https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html#sklearn.decomposition.PCA
@author: staar
"""
#%%
import numpy as np
from sklearn.decomposition import PCA
X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
X

#%%
covX = np.cov(X.T)
covX
"""
array([[5.6, 3.6],
       [3.6, 2.4]])
"""
#%% PCA
pca = PCA(n_components=2)
pca.fit(X)
print(pca.explained_variance_ratio_)  # [0.99244289 0.00755711]
print(pca.singular_values_)

#%% check it
ss = pca.singular_values_
ss2 = ss**2
ss2/sum(ss2)  # [0.99244289 0.00755711]

S = np.diag(ss)
S

U = pca.components_
U.T.dot(S).dot(U)
U.T.dot(S**2).dot(U)
U.dot(S).dot(U.T)
U.dot(S**2).dot(U.T)

# ???

#%%
pca = PCA(n_components=2, svd_solver='full')
pca.fit(X)
pca.explained_variance_ratio_  # array([0.99244289, 0.00755711])
ss = pca.singular_values_  # array([6.30061232, 0.54980396])
pca.components_

#%%
pca = PCA(n_components=2, svd_solver='arpack')



#%%




#%%


