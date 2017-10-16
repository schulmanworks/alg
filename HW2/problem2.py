#!/usr/bin/python
import timeit
import numpy as np
import math
import  matplotlib.pyplot as plt
import pdb

# minimum = -1
# good_path = {}
minimum=99999999
def path_len(path):
    result = 0
    # pdb.set_trace()
    length = len(path)
    for x in range(0, length - 1, 1):
        cost = path_dict[path[x]][path[x+1]]
        result += cost
    cost = path_dict[path[length-1]][path[0]]
    result += cost
    return cost

def getPath(good_paths, cur_path, cur_val,  cur_key, n, path_dict):
    global minimum
    global numPaths
    # print "cur_key", cur_key
    # print "cur_path", cur_path
    # pdb.set_trace()
    if cur_key not in cur_path:
        if cur_key != 0:
            cur_path.append(cur_key)
        for path in range(1, n+1, 1):
            if path in cur_path:
                if path != cur_key:
                    if len(cur_path) == n:
                        tmp = path_len(cur_path)
                        print cur_path, ":",tmp
                        if tmp < minimum:
                            minimum = tmp
                            good_paths.append(cur_path)
                            while len(good_paths) > 1:
                                good_paths.pop(0)

            else:
                # print "path", path
                # print "path_dict", path_dict
                # print "cur_key", cur_key
                cur_val = {}
                if cur_key == 0:
                    t = path + 1 if path + 1 <= 4 else 1
                    cur_val = {path : path_dict[path][t]}
                else:
                    cur_val = {path : path_dict[cur_key][path]}
                getPath(good_path, list(cur_path), cur_val, path, n, path_dict)

if __name__ == "__main__":
    path_dict = {
        1: {2:1, 3:2, 4:3},
        2: {1:1, 3:3, 4:4},
        3: {1:2, 2:3, 4:5},
        4: {1:3, 2:4, 3:5}
    }
    good_path = []
    getPath(good_path, [], {}, 0, 4, path_dict)
    print "good path = ", good_path
    # for x in range(4):
    #     for y in range(4):
    #         if y != x:
    #                 G.add_edge(x,y,weight=random.randint(0,10))
