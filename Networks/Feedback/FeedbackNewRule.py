import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
"""
#N = number of nodes 
#c = average degree
N = 10000
c=4
timeRange = 100

#generate random directed network
#set random weights of +1 or -1 & set all nodes active
G = nx.fast_gnp_random_graph(N,c/N,directed=True)
nx.set_edge_attributes(G, {e: {'weight': np.random.choice([-1,1])} for e in G.edges})
nx.set_node_attributes(G,{n: {"active": 1} for n in G.nodes})

#If a node has more active promoters than opressers, it will be active.
def updateGraph(G):
    #the list of nodes we will change the activity of
    changeNodes = []

    for node in G.nodes:
        #sum all the weights of the links which come from an active node 
        edgeSum = 0
        for link in G.in_edges(node,data=True):
            edgeSum += link[2]["weight"]*G.nodes[link[0]]["active"]
        changeNodes.append([node,edgeSum])
    for nodeActivity in changeNodes:
        G.nodes[nodeActivity[0]]["active"] += nodeActivity[1]

#calculate the ratio of active nodes to all nodes
def ratioActive(G,N):
    numactive = 0
    for node in G.nodes:
        if G.nodes[node]["active"]>0:
            numactive += 1
    return (numactive/N)



listt = []
listR = []

for t in range(timeRange):  
    listR.append(ratioActive(G,N))
    listt.append(t)
    updateGraph(G)
    

plt.plot(listt,listR)
plt.xlabel('$t$')
plt.ylabel('$R$')
plt.show()
"""
N = 2
M = np.random.randint(-1,2,(N,N))
v = np.random.randint(0,2,(N,1))


def ratioActive(v,N):
    numactive = 0
    for elem in v:
        if elem > 0:
            numactive += 1
    return (numactive/N)

listR = []
listT = range(100)
for t in listT:
    listR.append(ratioActive(v,N))
    v = np.matmul(M,v)

plt.plot(listT,listR)
plt.xlabel('$t$')
plt.ylabel('$R$')
plt.show() 