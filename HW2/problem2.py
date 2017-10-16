#!/usr/bin/python
import timeit
import numpy as np
import math
import  matplotlib.pyplot as plt
import pdb

minimum = -1
good_path = {}
def path_len(path):
    result = 0
    for dest in path:
        cost = dest[dest.keys()[0]]
        result += cost
    return cost

def getPath(cur_path, cur_val, n, path_dict):
    cur_key = cur_val.keys())[0]
    if list(cur_key not in cur_path:
        if cur_val is not None:
            cur_path.append(cur_val)
        for path in path_dict.keys():
            if len(cur_path) == n:
                tmp = path_len(cur_path)
                minimum = min(tmp, minimum)
                good_path = cur_path if tmp < minimum else good_path
            else:
                cur_val = {path : path_dict[cur_key][path]}
                getPath(list(cur_path), cur_val, n, path_dict)

if __name__ == "__main__":
    path_dict = {
        "A": {"B":1,"C":2,"D":3}
    }
