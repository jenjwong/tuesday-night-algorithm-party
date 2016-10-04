import networkx as nx
import collections
import matplotlib.pyplot as plt
import pygraphviz

# In order to get the visualization to run, install graphviz, and probably any graphviz-related
# dev files, as well as networkx, matplotlib, pygraphviz (also -dev).

# The node labels are (x, y, z), with x being the order that nodes are added to the tree, y is 
# the cumulative sum on that node, and z is the coin being used on that branch

def Tree():
    return collections.defaultdict(Tree)
    
def go_down(node, coins, cumulative, root):
    # print 'down', node, coins, cumulative
    cumulative += coins[0]
    # if cumulative == 6:
    #     print 'seis', node, coins, cumulative
    if cumulative > target:
        count = go_up(node, coins, cumulative - coins[0], root)
        coins = coins[1:]
             
    else:
        n = len(DG)
        # if cumulative == 6:
        # print 'seis', n, cumulative, coins[0], node
        DG.add_edge(node, (n,cumulative, coins[0]))
        count = go_down((n,cumulative, coins[0]), coins, cumulative, root)
    
    if cumulative == target:
        count += 1
        print'a huever'
    return count
    
def go_up(node, coins, cumulative, root):
    # print 'up', node, coins, cumulative
    
    # print node, coins
    if (DG.predecessors(node) == root) or (len(coins) == 1):
        return 0
        
    parent = DG.predecessors(node)[0]
    cumulative -= coins[0]
    if cumulative > 0:
        count = go_up(parent, coins, cumulative, root)
    if cumulative + coins[1] <= target:
        root = parent
        count = go_down(parent, coins[1:], cumulative, root)
        return count
    return count
    
def test_dg(node1, node2):
    DG.add_edge(node1, node2)
    return

def make_change(amount, coins):
    coins = coins[:]
    if not coins:
        return 0

    coin = coins.pop()
    count = 0

    tmp_amount = amount
    while (tmp_amount > 0):
        count += make_change(tmp_amount, coins)
        tmp_amount -= coin

    if tmp_amount == 0:
        count += 1

    return count
    
    
if __name__ == "__main__":
    target, coins = 20, [2,5]
    print make_change(target, coins)
    # node = (1, coins[0])
    node_init = 0
    DG=nx.DiGraph()
    DG.add_node(node_init)
    cumulative = 0
    
    # count = go_down(node_init, coins, cumulative)
    # for i in range(len(coins)):
    count = go_down(node_init, coins, cumulative, node_init)
    print count
    
    # test_dg(1,7)
    # test_dg(2,3)
    # pos1 = nx.nx_pydot.graphviz_layout(DG, prog='neato')
    pos2 = nx.nx_pydot.graphviz_layout(DG, prog='dot')
    plt.figure('get change')
    plt.clf()
    nx.draw(DG, pos = pos2, with_labels = True, alpha = 0.25, node_color = 'gray')
    plt.show()
