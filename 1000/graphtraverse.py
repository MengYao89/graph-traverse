
import time
start=time.time()
#!usr/bin/env python
#-*- coding:utf-8 -*-

from collections import deque


def read_adj_matrix(filename = 'AdjacencyMatrix_of_Graph_G.txt'):
    '''Read adjacency matrix of a graph from a txt file.'''
    res = []
    for ln in open(filename):
        if ln.strip() != '':
            res.append(ln.split())
    return res

def read_node_info(filename = 'Node_Information_of_Graph_G.txt'):
    '''Read node information from file. node information contains
    (Node #, city name, population, highest elevation).'''
    res = []
    for ln in open(filename):
        ln = ln.strip()
        
        if ln != '' and not 'Node#' in ln:
            items = ln.split()[1:]
            '''while '' in items:
                items.remove('')
            for i in range(len(items)):
                items[i] = items[i].strip()'''
            #print(items)
            res.append(tuple(items))
    return res

def read_source_stop_condition(filename = 'SourceNode_StoppingCondition.txt'):
    '''Read source node number and stopping condition.'''
    nodes = []
    conds = []
    for ln in open(filename):
        ln = ln.strip()
        if ln != '' and not 'Node#' in ln:
            #print (ln.split(maxsplit=1))
            node, cond = ln.split(None, 1)[0], \
                         ln.split(None, 1)[1].strip('"')
            cond = cond.replace('pop.', 'pop')
            cond = cond.replace('< =', '<=')
            cond = cond.replace('> =', '>=')
            nodes.append(int(node))
            conds.append(cond)
    return nodes, conds

def bfs(adjmat, nodeinfo, source, cond):
    '''Start from source node, find first node (city) in breadth that satisfies
    the given condition.'''

    path = []
    # Number of nodes
    n = len(nodeinfo)
    mark = [0 for i in range(n)] # mark whether a node has been visited
    # A queue to temporally store nodes that would be visited later.
    dq = deque()
    dq.append(source)
    while len(dq) > 0:
        node = dq.popleft()
        #print('visited', node)
        path.append(node)  # record path
        mark[node-1] = 1
        pop = int(nodeinfo[node-1][1]) # population
        elevation = float(nodeinfo[node-1][2])
        if eval(cond) == True:
            # stop condition satisfied
            #print ('City: ' + nodeinfo[node-1][0], 'Pop: ' + \
            #       nodeinfo[node-1][1], 'Elavation: ' + nodeinfo[node-1][2])
            break            
        for j in range(n):
            if adjmat[node-1][j] == '1' and not mark[j]:
                dq.append(j + 1)
                mark[j] = 1
    return path  
        
    

def dfs(adjmat, nodeinfo, source, cond):
    '''Start from source node, find first node (city) in breadth that satisfies
    the given condition.'''
    
    # Number of nodes
    n = len(nodeinfo)
    mark = [0 for i in range(n)]
    # A stack to temporally store nodes that would be visited later.
    dq = deque()
    dq.append(source)
    node = None
    while len(dq) > 0 or node:
        if not node: # go back on step
            node = dq.pop()
        #print('visited', node)        
        mark[node-1] = True
        pop = int(nodeinfo[node-1][1]) # population
        elevation = float(nodeinfo[node-1][2])
        
        if eval(cond) == True: # find target
            # stop condition satisfied
            #print ('City: ' + nodeinfo[node-1][0], 'Pop: ' + \
#                   nodeinfo[node-1][1], 'Elavation: ' + nodeinfo[node-1][2])\
            dq.append(node)
            break
        else: # go one step deeply
            dq.append(node)
            t = node
            node = None
            for j in range(n):
                if adjmat[t-1][j] == '1' and not mark[j]:
                    node = j + 1
                    break                
    return list(dq)  
        
def call_search_method(adjmat, nodeinfo, sources, conditions):
    '''Call breadth first and depth first search methods.'''
    dfsres = []
    bfsres = []
    for source, cond in zip(sources, conditions):
        dfsres.append(dfs(adjmat, nodeinfo, source, cond))
        bfsres.append(bfs(adjmat, nodeinfo, source, cond))
        
    f = open('Result_of_DFS_from_Source_to_Target_N_'+str(len(nodeinfo))+\
             '.txt', mode='w')
    
    for node in dfsres[0]:
        f.write('(City: %s, Pop: %s, Elevation: %s)\n'%nodeinfo[node-1])
    f.close()
    
    f = open('Result_of_BFS_from_Source_to_Target_N_'+str(len(nodeinfo))+\
             '.txt', mode='w')
    for node in bfsres[0]:
        f.write('(City: %s, Pop: %s, Elevation: %s)\n'%nodeinfo[node-1])
    f.close()    
    
    return dfsres, bfsres


if __name__ == '__main__':    
    
    adjmat = read_adj_matrix()
    #print (adjmat)
    nodeinfo = read_node_info()
    #print(nodeinfo)
    sources, conditions = read_source_stop_condition()
    #print(sources, conditions)
    
    dfsres, bfsres = call_search_method(adjmat, nodeinfo, sources, conditions)
    print('DFS:', dfsres)
    print ('BFS:', bfsres)
    
print (time.time()-start)
