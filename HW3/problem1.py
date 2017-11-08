#!/usr/bin/python
import timeit
import numpy as np
import math
import  matplotlib.pyplot as plt
import pdb
import random

def getKthElement(k , arr):
    localMaxIndex = 0
    localMax = arr[localMaxIndex]

    # scan first portion
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    for i in range(k):
        if arr[i] > localMax:
            localMax = arr[i]
            localMaxIndex = i
    tmp_arr = arr[k:]
    while len(tmp_arr) > 0:
        if tmp_arr[0] < localMax:
            arr[localMaxIndex] = tmp_arr[0]
            del tmp_arr[0]
            return getKthElement(k, arr[:k]+tmp_arr)
        else:
            del tmp_arr[0]
    return localMax

if __name__ == "__main__":
    avgs = []
    v = 10000
    k = 10
    x_axs = range(k,v,1)
    for x in x_axs:
        avg = 0
        r = 100
        for __ in range(r):
            arr = [random.randint(0,100) for _ in range(x)]
            start_time = timeit.default_timer()
            element = getKthElement(k, arr)
            elapsed = timeit.default_timer() - start_time
            avg += elapsed
        avg /= float(r)
        avgs.append(avg)

    plt.plot(x_axs, avgs)
    plt.show()
