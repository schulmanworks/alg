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
    arr = [random.randint(0,100) for _ in range(10)]
    k = 3
    print arr
    print sorted(arr)
    element = getKthElement(k, arr)
    print element
