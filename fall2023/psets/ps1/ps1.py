from asyncio import base_tasks
import math
import time
import random

"""
See below for mergeSort and countSort functions, and for a useful helper function.
In order to run your experiments, you may find the functions random.randint() and time.time() useful.

In general, for each value of n and each universe size 'U' you will want to
    1. Generate a random array of length n whose keys are in 0, ..., U - 1
    2. Run count sort, merge sort, and radix sort ~10 times each,
       averaging the runtimes of each function. 
       (If you are finding that your code is taking too long to run with 10 repitions, you should feel free to decrease that number)

To graph, you can use a library like matplotlib or simply put your data in a Google/Excel sheet.
A great resource for all your (current and future) graphing needs is the Python Graph Gallery 
"""


def merge(arr1, arr2):
    sortedArr = []

    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i >= len(arr1):
            sortedArr.append(arr2[j])
            j += 1
        elif j >= len(arr2):
            sortedArr.append(arr1[i])
            i += 1
        elif arr1[i][0] <= arr2[j][0]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    return sortedArr

def mergeSort(arr):
    if len(arr) < 2:
        return arr

    midpt = int(math.ceil(len(arr)/2))

    half1 = mergeSort(arr[0:midpt])
    half2 = mergeSort(arr[midpt:])

    return merge(half1, half2)

def countSort(univsize, arr):
    universe = []
    for i in range(univsize):
        universe.append([])

    for elt in arr:
        universe[elt[0]].append(elt)

    sortedArr = []
    for lst in universe:
        for elt in lst:
            sortedArr.append(elt)

    return sortedArr

def BC(n, b, k):
    if b < 2:
        raise ValueError()
    digits = []
    for i in range(k):
        digits.append(n % b)
        n = n // b
    if n > 0:
        raise ValueError()
    return digits

def radixSort(univsize, base, arr):
    n = len(arr)
    k = int(math.ceil(math.log(univsize, base)))
    v = []
    arr_with_digit = []
    digits = []
    for i in range(n):
        v.append(BC(arr[i][0], base, k))
        digits.append([0])
    for i in range(n):
        arr_with_digit.append((digits[i], (arr[i][1], i)))
    for j in range(k):
        for i in range(n):
            digits[i] = v[i][j]
        for i in range(n):
            digits_index = arr_with_digit[i][1][1]
            arr_with_digit[i] = (digits[digits_index], arr_with_digit[i][1])
        arr_with_digit = countSort(base, arr_with_digit)
    result = []
    for i in range(n):
        b, total = 1, 0
        for digit in range(len(v[i])):
            total = total + v[arr_with_digit[i][1][1]][digit] * b
            b = b * base
        result.append((total, arr_with_digit[i][1][0]))
    # print(result)
    return result

# radixSort(30, 6, [(4,4),(9,9),(8,8),(7,7),(21,21)])