
#%%
import numpy as np
from scipy.linalg import eig

import matplotlib.pyplot as plt
import numpy as np
import timeit
import math
import random

def pagerankeig(probtransition):
    """calculates pagerank using left principal eigen vector method
    ______
    
    Parameters
    ------
    probtransition : Probability transition matrix
    
    Returns
    ------
    pagerank : the page rank calculated by eigen vector method"""
    
    w, vl, vr=eig(probtransition, left=True)
    #calculate eigen values (w) and left eigen vectors(vl)

    sorted_index = np.argsort(w)[::-1]
    sorted_eigenvalue = w[sorted_index]
    sorted_eigenvectors = vl[:,sorted_index]
    #sorted eigen vectors according to descending eigen values

    pagerank=sorted_eigenvectors[:,0]/sorted_eigenvectors[:,0].sum()
    #set the pageranks calculated by eigen vector method
    
    return pagerank


def poweritr(p,tr, itr=100):
    """recursive function to calculate the pagerank using power iteration
    ______
    
    Parameters
    ------
    p : initial page rank vector
    tr : Probability transition matrix
    itr : number of iterations, default=100
    
    Returns
    ------
    pagerank : the page rank calculated by power iteration method"""
    
    
    pnew=np.dot(p,tr)
    var=((pnew-p)**2).sum()
    itr-=1
    if itr>0:
        return poweritr(pnew,tr, itr)
    else:
        return pnew

plt.rcParams['figure.figsize'] = [10, 6] # set size of plot

ns = np.linspace(1, 1000, 100, dtype=int)
print(ns)
ts = [timeit.timeit('pagerankeig(probtransition)', 
                    setup='probtransition=np.ones(({},{}))'.format(n,n),
                    globals=globals(),
                    number=1)
      for n in ns]
plt.plot(ns, ts, 'or')
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-b')
'''
ns = np.linspace(1, 5000, 500, dtype=int)
print(ns)
ts = [timeit.timeit('poweritr(p,tr)', 
                    setup='tr=np.zeros(({},{})); p=np.ones((1,{}));'.format(n,n,n),
                    globals=globals(),
                    number=1)
      for n in ns]
plt.plot(ns, ts, 'og')
degree = 4
coeffs = np.polyfit(ns, ts, degree)
p = np.poly1d(coeffs)
plt.plot(ns, [p(n) for n in ns], '-r')
'''
#%%