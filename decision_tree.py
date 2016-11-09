import numpy as np
import random
import matplotlib.pyplot as plt

def neighbours(node, n):
    # return neighbours to node = (x,y) in a grid of size n x n
    x,y = node
    x_new, y_new = [], []
    neighs = []
    if x>0:
        if y>0:
            if x < n-1:
                if y < n-1:
                    neighs += [(x+1,y), (x-1,y), (x,y+1), (x, y-1)]
                else:
                    neighs += [(x+1,y), (x-1,y), (x, y-1)]
            else:
                if y < n-1:
                    neighs += [(x-1,y), (x,y+1), (x, y-1)]
                else:
                    neighs += [(x-1,y), (x, y-1)]
        else:
            if x < n-1:
                neighs += [(x+1,y), (x-1,y), (x,y+1)]
            else:
                neighs += [(x-1,y), (x,y+1)]
    else:
        if y>0:
            if y <  n-1:
                neighs += [(x+1,y), (x,y+1), (x,y-1)]
            else:
                neighs += [(x+1,y), (x,y-1)]
        else:
            neighs += [(x+1,y), (x,y+1)]
    return set(neighs)
    
plt.figure('trajectory')
plt.clf()
for i in range(1000):
    n = 100
    node = (n//2,n//2)
    visited_nodes = [node]
    neighs = neighbours(node, n)
    step_counter = 0
    while neighs and node != (n-1,n-1):
        node = list(neighs)[random.choice(range(len(neighs)))]  # for more rand
        visited_nodes.append(node)
        neighs = neighbours(node, n) - set(visited_nodes) 
        step_counter += 1
    
    x,y = np.array([i[0] for i in visited_nodes]), np.array([i[1] for i in visited_nodes])
    x_rand = 0.1*np.random.randn(len(x))
    y_rand = 0.1*np.random.randn(len(x))
    plt.plot(x + x_rand,y + y_rand, '-', color='black', lw = 0.2, alpha=1)
    plt.axis([-1,n,-1,n])
plt.show()