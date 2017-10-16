#!/usr/bin/python
import timeit
import numpy as np
import math
import  matplotlib.pyplot as plt
import pdb
import networkx as nx
import random

minimum=99999999

def path_len(path, G):
    print path
    # pdb.set_trace()
    result = 0
    length = len(path)
    for x in range(0, length - 1, 1):
        cost = G[path[x]][path[x+1]]["weight"]
        result += cost
    cost = G[path[length-1]][path[0]]["weight"]
    result += cost
    return cost
def getPath(G, n, good_path, curPath = [], curNode=None):
    global minimum
    if curNode is None:
        for node in G.nodes():
            getPath(G, n, good_path, curPath = [], curNode=node)
    else:
        if curNode not in curPath:
            # print "curNode", curNode
            curPath.append(curNode)
        else:
            return
        for edge in G.edges(curNode):
            node = edge[1]
            if len(curPath) == n:
                tmp = path_len(curPath, G)
                # print curPath, ":",tmp
                if tmp < minimum:
                    minimum = tmp
                    good_path.append(curPath)
                    while len(good_path) > 1:
                        good_path.pop(0)
            else:
                getPath(G, n, good_path, curPath=list(curPath), curNode=node)

if __name__ == "__main__":
    good_path = []
    G = nx.Graph()
    n = 4
    for x in range(n):
        for y in range(n):
            if y != x:
                    G.add_edge(x,y,weight=random.randint(1,10))
    getPath(G, n, good_path)
    print "good_path", good_path
    # pdb.set_trace()