import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

c = 4
N_values = [100,1000,10000,100000]

def link_percolation(G, p):
    G_copy = G.copy()
    num_edge = len(G.edges())
    num_edge_deleted = round((1-p) * num_edge)
    edge_list = np.random.permutation(list(G.edges()))
    G_copy.remove_edges_from(edge_list[1:num_edge_deleted])
    comp_gen = nx.connected_components(G_copy)
    largest_cc = len(max(nx.connected_components(G_copy), key=len))
    R = (largest_cc/N)
    return R

def genList(G,N):
    list_R = []
    list_p = []
    for p in np.linspace(0, 1, 101):
        R_values = []
        for i in range(int(100000/N)):
            R = link_percolation(G, p)
            R_values.append(R)
        meanR = np.mean(R_values)
        list_p.append(p)
        list_R.append(meanR)
    return [list_p,list_R]

if __name__ =="__main__":
    for N in N_values:
        G = nx.erdos_renyi_graph(N,c/N)
        listValues = genList(G,N)
        plt.plot(listValues[0],listValues[1],label = "N = " + str(N))
    plt.legend()
    plt.title("Link Percolation on Different Sized Random Networks")
    plt.xlabel('$p$ - probability of retaining a link')
    plt.ylabel('$R$ - size of the giant component')
    plt.show()

