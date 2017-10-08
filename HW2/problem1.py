#!/usr/bin/python
import timeit
import numpy as np
import math
import  matplotlib.pyplot as plt
import pdb
testArr = [2,7,6,9,5,1,4,3,8]

def check(arr, n):
    magicNumber = n * (n * n + 1) / 2.0
    # print "magicNumber", magicNumber
    # print arr
    # should_pass = False
    # if testArr == arr:
    #     print "should have passed"
    #     should_pass = True
        # pdb.set_trace()
    for x in range(n):
        # check rows
        summ = np.sum(arr[x*n:x*n + n])
        if summ != magicNumber:
            return False
        # check columns
        tempArr = [arr[y] for y in range(x, n*n, n)]
        summ = np.sum(tempArr)
        if summ  != magicNumber:
            return False
    # check diagonals
    tempArr = [arr[x] for x in range(0, n*n, n+1)]
    summ = np.sum(tempArr)
    if summ != magicNumber:
        return False
    tempArr = [arr[x] for x in range(n-1, n*n - n + 1, n-1)]
    summ = np.sum(tempArr)
    if summ != magicNumber:
        return False
    return True



def getMagicSquares(n, good_arrs, cur_val=0, cur_arr=[]):
    # print cur_arr
    # print cur_val
    if cur_val not in cur_arr:
        if cur_val != 0:
            cur_arr.append(cur_val)
        # print "cur_arr", cur_arr
        # print "depth: ", len(cur_arr)
        # print "cur_val", cur_val
        # print "range", range(cur_val + 1, n, 1)
        rr = range(1, n*n + 1, 1)
        # print rr
        for x in rr:
            if len(cur_arr) == n*n:
                # print "found right length"
                if check(cur_arr, n):
                    print "passed check"
                    good_arrs.append(cur_arr)
            else:
                getMagicSquares(n, good_arrs, x, list(cur_arr))

if __name__ == "__main__":
    good_arrs = []
    n = 3
        # pdb.set_trace()
    getMagicSquares(n, good_arrs, cur_arr=[])
    print good_arrs
