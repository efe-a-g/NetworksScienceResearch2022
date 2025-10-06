import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

#N = number of nodes
#graphperc = number of graphs egnerated per c value to obtain average fixed point
N = 1000
graphperc = 100

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


listTAve= []
listc = range(20)
for c in listc:
    listT = []
    for i in range(graphperc):
        #variables to track the ratio active at each stage
        rBefore = 0
        rNow = 1
        t=0
        #generate random directed network
        #set random weights of +1 or -1 & set all nodes active
        G = nx.fast_gnp_random_graph(N,c/N,directed=True)
        #G = nx.scale_free_graph(N,)
        nx.set_edge_attributes(G, {e: {'weight': np.random.choice([-1,1])} for e in G.edges})
        nx.set_node_attributes(G,{n: {"active": True} for n in G.nodes})
        #update graph until a stable ratio is reached
        while rNow != rBefore: 
            t+=1 
            updateGraph(G)
            rBefore = rNow
            rNow = ratioActive(G,N)
        listT.append(t)
    listTAve.append(np.mean(listT))
plt.plot(listc,listTAve)
plt.xlabel('$N$')
plt.ylabel('$T$')
plt.show()
