#!/usr/bin/python
import timeit
import numpy as np
import math
import  matplotlib.pyplot as plt
import pdb
import random
from heapq import merge

inversions = 0

def sort(arr):
    global inversions
    if arr[0] > arr[1]:
        return [arr[1], arr[0]]
    else:
        return arr
def merge(a, b):
    global inversions
    result = []
    total = len(a) + len(b)
    i = j = 0
    for x in range(total):
        if i == len(a):
            result += b[j:]
            break
        elif j == len(b):
            result += a[i:]
            break
        elif a[i] < b[j]:
            inversions += 1
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    return result

def mergeSort(arr):
    global inversions
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return sort(arr)
    a = mergeSort(arr[:len(arr)/2])
    b = mergeSort(arr[len(arr)/2:])
    m = merge(a,b)
    return m

if __name__ == "__main__":
    x = 10
    arr = [2, 4, 1, 3, 5]#
    # arr = [random.randint(0,100) for _ in range(x)]
    # print arr
    res = mergeSort(arr)
    print "$$$$$$$$$$$$$$"
    print "array",arr
    print "result",res
    print "inversions:", inversions

    avgs = []
    v = 1000
    k = 10
    x_axs = range(k + 1,v,1)
    for x in x_axs:
        avg = 0
        r = 100
        for __ in range(r):
            arr = [random.randint(0,100) for _ in range(x)]
            start_time = timeit.default_timer()
            res = mergeSort(arr)
            elapsed = timeit.default_timer() - start_time
            # print res
            avg += elapsed
        avg /= float(r)
        avgs.append(avg)

    plt.plot(x_axs, avgs)
    plt.show()
