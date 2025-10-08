#The maximum sum subarray problem consists in finding the maximum sum of a contiguous 
# subsequence in an array or list of integers:

#Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#Output: 6 (Sum of [4, -1, 2, 1])

#Easy case is when the list is made up of only positive numbers and the maximum 
# sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.
#  Your solution should be fast, it will be tested on very large arrays so slow solutions will time out.

#Empty list is considered to have zero greatest sum.
#Note that the empty list or array is also a valid sublist/subarray.


def max_sequence(arr):
    a = 0
    b=0
    for i in arr:
        b = max(0,b+i)
        a = max(a,b)
    return a
print(max_sequence(arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]))

