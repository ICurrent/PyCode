# Search Algorithms: Linear search, Interpolation search, Binary search

# Linear Search
from ast import Nonlocal


def linear_search(list, search_for):
    count = 0
    result = False

    while count < len(list) and result == False:
        if search_for in list:
            return True
        else:
            return False
        count += 1

print(linear_search([2, 6, 7, 8], 2))
print(linear_search([2, 6, 7, 8], 5))



# Binary Search
# def binary_search(list, val):
#     size = len(list) - 1l
#     idxo = 0
#     idxn = size

#     # find the middle most value
#     while idxo <= idxn:
#         midval = (idxo + idxn) // 2
#         if list(midval) == val:
#             return midval

#     # compare the value the middle most value:
#     if val > list(midval):
#         idxo = midval - 1
#     else:
#         idxn = midval - 1

#     if idxo > idxn:
#         return None

# list = [2, 7, 19, 3, 8]
# print(binary_search(list, 7))