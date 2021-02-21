"""
Problem: Given an array a = [1, 2, 3, 4, 5, 6, 7, 8]
find the number 8. Using a binary search algorithm
Assume that the list is sorted.
"""

from typing import Union

def binarySearch(array: list, target: int) -> Union[int, None]:
    origin = 0
    endpoint = len(array) - 1

    while origin <= endpoint:
        midpoint = origin + (endpoint - origin) // 2
        print(f"Midpoint: {midpoint}")
        if array[midpoint] == target:
            return midpoint

        elif array[midpoint] > target:
            endpoint = midpoint - 1

        else: # array[midpoint] < target
            origin = midpoint + 1

    return None


a = [1, 2, 3, 4, 5, 6, 7, 8]
out = binarySearch(a, 6)

