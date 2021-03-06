#!/usr/bin/python
import timeit
import numpy as np
import math
import  matplotlib.pyplot as plt
def genArray(l):
    arr = np.random.random_integers(low=0, high=100e3, size=l)
    return np.sort(arr)
def binarySearch(A, l, h, key):
    if len(A) == 0:
        return None
    if l > h:
        return None
    m = int(math.floor((h+l)/2))
    if m == len(A):
        return None
    if A[m] == key:
        return A[m]
    elif A[m] < key:
        return binarySearch(A, m+1, h, key)
    else:
        return binarySearch(A, l, m-1, key)

if __name__ == "__main__":
    numShouldFind = 0
    numFound = 0
    times = []
    r = range(1, 1000000, 5000)
    for x in r:
        arr = genArray(x)
        avg = 0
        runs = 1000
        rng = range(runs)
        for v in rng:
            num = np.random.randint(low=0, high=x)
            start_time = timeit.default_timer()
            found = binarySearch(arr, 0, x, num) is not None
            if found:
                numFound += 1
                avg += elapsed
            else:
                # we want a redo if we don't fine it
                rng = range(runs + 1)
            if num in arr:
                numShouldFind += 1
            elapsed = timeit.default_timer() - start_time

        avg = avg/runs
        print "avg elapsed time: %f" % (avg)
        times.append(avg)
    print "numShouldFind", numShouldFind
    print "numFound", numFound
    plt.plot(r, times)
    plt.show()
