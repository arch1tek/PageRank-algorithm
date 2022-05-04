
#%%
import numpy as np
from pagerankfx import pagerank
import networkx as nx
class Graph:
    """graph containing nodes numbered 1 to number of nodes (`Graph.numofnodes`) and (`Graph.numofconnections`) edges"""
    
    #: number of nodes in the graph
    numofnodes: int
    #: number of edges/connections in the graph
    numofconnections: int
    
    def __init__(self, nn, nc):
        self.numofnodes=nn
        self.numofconnections=nc
        #: adjacency matrix
        self.adjmatrix=np.zeros((self.numofnodes,self.numofnodes))
       
        
    def addconnection(self,a,b):
        """updates adjacency matrix (`Graph.adjmatrix`) with an edge directed from a to b"""
        self.adjmatrix[a-1,b-1]=self.adjmatrix[a-1,b-1]+1
    
if __name__ == "__main__":
    nn=int(input("enter number of nodes: "))
    """take number of nodes as input"""

    nc=int(input("enter number of connections: "))
    """take number of connections as input"""

    g=Graph(nn,nc)
    
    for x in range(nc):
        print("connction "+str(x+1))
        a=int(input("from: "))
        b=int(input("to: "))
        g.addconnection(a,b)
        
    graph=nx.from_numpy_matrix(g.adjmatrix, parallel_edges=True,  create_using=nx.DiGraph)
    mapping = {}
    for i in range(g.numofnodes):
        mapping[i]=i+1
    graph=nx.relabel_nodes(graph, mapping)
    nx.draw(graph, with_labels=True, arrows = True, connectionstyle='arc3, rad = 0.1')
    pagerank(g.adjmatrix, g.numofnodes)
#%%