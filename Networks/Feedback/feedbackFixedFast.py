import numpy as np
import networkx as nx

#N = number of nodes 
#rangeC = range of c values investigated
#graphperC = number of graphs egnerated per c value to obtain average fixed point
N = 500
rangeC = 20
graphperC = 20

#If a node has more active promoters than opressers, it will be active.
def updateGraph(G):
    #the list of nodes we will change the activity of
    changeNodes = []

    for node in G.nodes:
        #sum all the weights of the links which come from an active node 
        edgeSum = 0
        for link in G.in_edges(node,data=True):
            if G.nodes[link[0]]["active"]:
                edgeSum += link[2]["weight"]
        if edgeSum > 0:
            changeNodes.append([node,True])
        elif edgeSum < 0:
            changeNodes.append([node,False])
        else:
            pass
    for nodeActivity in changeNodes:
        G.nodes[nodeActivity[0]]["active"] = nodeActivity[1]

#calculate the ratio of active nodes to all nodes
def ratioActive(G,N):
    numactive = 0
    for node in G.nodes:
        if G.nodes[node]["active"]:
            numactive += 1
    return (numactive/N)


listRAve= []
for c in range(rangeC):
    listR = []
    for i in range(graphperC):
        #variables to track the ratio active at each stage
        rBefore = 0
        rNow = 1
        #generate random directed network
        #set random weights of +1 or -1 & set all nodes active
        G = nx.fast_gnp_random_graph(N,c/N,directed=True)
        nx.set_edge_attributes(G, {e: {'weight': np.random.choice([-1,1])} for e in G.edges})
        nx.set_node_attributes(G,{n: {"active": True} for n in G.nodes})
        #update graph until a stable ratio is reached
        while rNow != rBefore:  
            updateGraph(G)
            rBefore = rNow
            rNow = ratioActive(G,N)
        listR.append(rNow)
    listRAve.append(np.mean(listR))
print(listRAve)
