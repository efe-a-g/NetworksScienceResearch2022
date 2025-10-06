import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import collections

#N = number of nodes 
#c = average degree of nodes
N = 10000
c = 5.76

#generate random network 
G = nx.fast_gnp_random_graph(N,c/N)

def updateGraph(G, threshold):
    changeNodes = []
    for node in G.nodes:
        failureNeighbours = 0
        neighbours = 0
        for neighbour in G.neighbors(node):
            if G.nodes[neighbour]["failure"] == 1:
                failureNeighbours += 1
            neighbours += 1
        if neighbours > 0 and G.nodes[node]["failure"] != 1:
            if failureNeighbours/neighbours >= threshold:
                changeNodes.append(node)
    for node in changeNodes:
        G.nodes[node]["failure"] = 1
    return changeNodes

listNodes = G.nodes
listFail = []
threshold = 0.18

for node in G.nodes:
    nx.set_node_attributes(G,{n: {"failure": 0} for n in G.nodes})
    G.nodes[node]["failure"] = 1
    newFail = 1
    totalFail = 0
    while newFail != 0:
        totalFail += newFail
        newFail = len(updateGraph(G,threshold))
    listFail.append(totalFail)
plt.plot(listFail,listNodes)

plt.hist(listFail,width=0.8)

degree_sequence = sorted(listFail, reverse=True)  # degree sequence
# print "Degree sequence", degree_sequence
degreeCount = collections.Counter(degree_sequence)
deg, cnt = zip(*degreeCount.items())
N = len(listNodes)
cnt = [item/N for item in cnt ]

x = np.log(deg)
y = np.log(cnt)

a, b = np.polyfit(x, y, 1)
plt.scatter(x, y)
plt.plot(x,a*x+b)
plt.xlabel("log(Failure Size)")
plt.ylabel("log(Frequency of Failure)")
plt.title("log-log Graph of the Frequency of Failure against the Size of the Failure")

print(a,b)