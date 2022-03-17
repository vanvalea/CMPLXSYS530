# Ethan VanValkenburg
# Problem 1

# Problem 1:  One-dimensional cellular automata
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from numpy import linalg as la
import math

''' 
CA with the following rules:
If all three cells in the neighborhood are 1’s, the center cell becomes a 0
If 2 of the 3 cells in the neighborhood are 1’s, become a 1
If precisely one of the neighbor cells are 1’s, and the center cell is a zero, become a 1
If only the center cell is a 1, become a 0
If all cells are 0’s, stay a 0
'''

# how should I express this/
rule1 = {
        (1,1,1):0,
        (1,1,0):1,
        (1,0,1):1,
        (0,1,1):1,
        (1,0,0):1,
        (0,0,1):1,
        (0,1,0):0,
        (0,0,0):0
        }

# which rule is this?
# what is the binary number rule and what does that mean?

#{}{}{}{}{}{}{}{}{}#
# part B
'''
Problem 1B) Implement the model in python with an 8-cell 1-dimensional grid, with wrapped boundaries (i.e. a ring). Explore the network phase space for this rule, and highlight the attracting subcomponents.

How many distinct basins of attraction are there?
What behaviors does each basin of attraction exhibit? E.g. do all the initial conditions lead to a constant steady state, or does the system approach an oscillation? If it does oscillate, how long is the period of the oscillation?
In your write-up, be sure to include plots of each network component (i.e. basin of attraction), with the attracting sub-component highlighted in another color, as well as a description of the model dynamics for each component.
'''

# how do I determine the initial conditions?
# config2int
def config2int(config):
    return int(''.join(map(str, config)),2)
# int2config
def int2config(x):
     # does it have something to do with counting backwards
     # REVIEW THESE BIT CONVERSIONS
     return [1 if x & 2**i > 0 else 0 for i in range(L - 1, -1, -1)]
    
# update
def update(config):
    nextconfig = [0]*L
    for x in range(L):
        nextconfig[x] = rule[(config[(x-1) % L], config[x],config[(x + 1) % L])]
    return nextconfig



# set up the conditions for the CA
initialcond = []
L = 8
rule = rule1



# run the model
steps = 20
output = np.zeros([steps,L]) #make a full matrix
output[0,:] = int2config(5)
for i in range(1,steps):
    output[i,:] = update(output[i-1,:])
plt.cla()
plt.imshow(output)
plt.show()



g = nx.DiGraph() # Make an empty graph that will be the phase space

for x in range(2**L):
    g.add_edge(x, config2int(update(int2config(x))))
    
# Plot each connected component of the phase space
ccs = [cc for cc in nx.connected_components(g.to_undirected())]
n = len(ccs)
w = math.ceil(math.sqrt(n))
h = math.ceil(n / w)
for i in range(n):
    plt.subplot(h, w, i + 1)
    nx.draw_networkx(nx.subgraph(g, ccs[i]), with_labels = True)

plt.show()
    
plt.clf()

# ANALYZE THE PHASE SPACE
for i,cc in enumerate(ccs):
    plt.clf()
    
    subg = nx.subgraph(g, cc)
    attr = set().union(*nx.attracting_components(subg))
    
    pos=nx.spring_layout(subg) # positions for all nodes
    # nx.draw_networkx_nodes(subg,pos, nodelist = (set(subg.nodes()) - attr), node_color='#00b4e9', node_size=500, alpha=0.8)
    # nx.draw_networkx_nodes(subg, pos, nodelist = attr, node_color='r', node_size=500, alpha=0.8)
    nx.draw_networkx_nodes(subg, pos, node_color=list(nx.degree_centrality(subg).values()), node_size=500, alpha=0.8)
    nx.draw_networkx_edges(subg,pos,width=2.0)
    nx.draw_networkx_labels(subg,pos)
    

    print("Loops in basin {} : {}".format(i, list(nx.simple_cycles(nx.subgraph(g,cc)))))
    
    plt.show()


