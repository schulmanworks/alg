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
    for i in range(k, len(arr)):
        if arr[i] < localMax:
            arr[localMaxIndex] = arr[i]
            del arr[i]
            return getKthElement(k, arr)
    return localMax

if __name__ == "__main__":
    arr = [random.randint(0,100) for _ in range(10)]
    k = 6
    print arr
    print sorted(arr)
    element = getKthElement(k, arr)
    print element
