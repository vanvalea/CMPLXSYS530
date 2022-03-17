# Problem 1:  One-dimensional cellular automata
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from numpy import linalg as la
import math

# create a dictionary of rules
CA_rules = {
# Rule 50

    50 : {
            (0,0,0):0,
            (0,0,1):1,
            (0,1,0):0,
            (0,1,1):0,
            (1,0,0):1,
            (1,0,1):1,
            (1,1,0):0,
            (1,1,1):0
            },
    

    # Rule 13
    
    13 : {
            (0,0,0):1,
            (0,0,1):0,
            (0,1,0):1,
            (0,1,1):1,
            (1,0,0):0,
            (1,0,1):0,
            (1,1,0):0,
            (1,1,1):0
            },
    

    
    # Rule 30
    30 : {
            (0,0,0):0,
            (0,0,1):1,
            (0,1,0):1,
            (0,1,1):1,
            (1,0,0):1,
            (1,0,1):0,
            (1,1,0):0,
            (1,1,1):0
            },

    # Rule 184 (Majority rule not counting self, with ties awarded to 1)

    184: {
            (0,0,0):0,
            (0,0,1):0,
            (0,1,0):0,
            (0,1,1):1,
            (1,0,0):1,
            (1,0,1):1,
            (1,1,0):1,
            (1,1,1):1
            }
}


for rule in CA_rules:
    
    
    neighrule = CA_rules[rule]
    
    
    # functions for the model
    # Takes a configuration and returns the corresponding integer
    #We'll start with two functions to convert between decimal integers and binary model configurations
    def config2int(config):
        return int(''.join(map(str, config)),2) #maps the config->strings, joins them, and then converts to int from binary
    
    # Takes an integer and converts it to a configuration (list of cell states)
    def int2config(x):
        return [1 if x & 2**i > 0 else 0 for i in range(L - 1, -1, -1)]
    
    
    def update(config):
        nextconfig = [0]*L
        for x in range(L):
            nextconfig[x] = neighrule[(config[(x - 1) % L],config[x],config[(x + 1) % L])]
        return nextconfig
    
    ### Set up some conditions to run the CA
    initialcond = [0,0,0,1,0,1,0,1,1,1] # for testing
    L = 5  #9 #10   # Grid size (start with something small)
    

    # Run the model
    # Run the model for a few steps and plot
    steps = 20
    output = np.zeros([steps,L])
    output[0,:] = int2config(6)
    for i in range(1,steps):
        output[i,:] = update(output[i-1,:])
    plt.cla()
    plt.imshow(output)
    plt.show()
    
    
    # Mapping out the phase space
    # what is the phase space?
    # exploring the phase space—where do initial conditions go next?
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
    
    


    # Suplots are sometimes too packed, so also useful to just draw a few individually
    #nx.draw_networkx(nx.subgraph(g, ccs[1]), with_labels = True)  
    
    



