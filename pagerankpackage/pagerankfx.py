from locale import normalize
from pydoc import pager
import numpy as np
from scipy.linalg import eig

alpha=0.1
'''teleportation factor \n
    default=0.1'''

def pagerank(adjmatrix, numofnodes):
    
    norm=adjmatrix.sum(axis=1)
    norm[norm==0]=1
    probtransition=(adjmatrix/norm[:,None]) 
    #normalize rows to calculate probability transition matrix from each page

    probtransition=probtransition*(1-alpha)
    probtransition=probtransition+(alpha/numofnodes)
    #new probability transition matrix taking teleportation into consideration

    print(probtransition)
    
    pagerank=pagerankeig(probtransition)
    #pagerank calculated by eigen method
    
    print("eigen vector method:\n")
    print("scores")
    print(np.around(pagerank, decimals=3, out=None))
    #print pagerank calculated by eigen vector method
    
    sorted_index = np.argsort(pagerank)[::-1]
    
    #: sort pages according to pagerank
    sorted_pages={}
    for i in range(numofnodes):
        sorted_pages[i+1]=sorted_index[i]+1
    print("ranks")
    print(sorted_pages)

    pagerankitr=np.ones((1,numofnodes))/numofnodes
    #initialize new pagerank vector with equal probabilities to be passed to power iteration function"""

    pagerankitr=poweritr(pagerankitr,probtransition, 100)
    #pagerank is calculated using power iteration method

    print("power iteration:\n")
    print("scores")
    print(np.around(pagerankitr, decimals=3, out=None))
    #print pagerank calculated by power iteration method
    
     #: sort pages according to pagerank
    sorted_pages={}
    for i in range(numofnodes):
        sorted_pages[i+1]=sorted_index[i]+1
    print("ranks")
    print(sorted_pages)
        
def pagerankeig(probtransition):
    """calculates pagerank using left principal eigen vector method
    
    ______
    
    Parameters
    ------
    probtransition : Probability transition matrix
    
    Returns
    ------
    pagerank : the page rank calculated by eigen vector method
    
    """

    
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
    itr=itr-1
    sumofcomp=np.sum(pnew)
    if sumofcomp==0:
        sumofcomp=1
    pnew=pnew/sumofcomp
    if itr>0:
        return poweritr(pnew,tr, itr)
    else:
        return pnew