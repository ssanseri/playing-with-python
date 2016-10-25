#!/usr/bin/env python

# stole this sort code from
# http://stackoverflow.com/questions/18262306/quick-sort-with-python
# no sense in reinventing the wheel
# code was written using xrange(), a python2 function, changed it to range()
def partition(array, begin, end):
    pivot = begin
    for i in range(begin+1, end+1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot

def quicksort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin >= end:
        return
    pivot = partition(array, begin, end)
    quicksort(array, begin, pivot-1)
    quicksort(array, pivot+1, end)

array1 = [67, 45, 2, 13, 1, 998]
quicksort(array1)
print(array1)

array2 = [89, 23, 33, 45, 10, 12, 45, 45, 45]
quicksort(array2)
print(array2)

#
#          Your sorted lists should look like this when displayed:
#          [1, 2, 13, 45, 67, 998]
#          [10, 12, 23, 33, 45, 45, 45, 45, 89]
