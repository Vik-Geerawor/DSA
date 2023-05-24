"""
You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list.
"""


def binary_search(input_array, value):
    """Your code goes here."""
    # find the length of the array, if length < 1, return -1
    # half the length, if even, take the lower index
    # if -1 < index < length
    # if value matches, return the index
    # else if value is <, half current index and go to step 3
    # else if value is >, (index + (length - index)/2) and go to step 3
    # else, return -1

    upper_index = len(input_array) - 1
    lower_index = 0
    if upper_index < 1:
        return -1
    else:
        index = (lower_index + upper_index) // 2
        while lower_index <= index <= upper_index:
            if value == input_array[index]:
                return index
            elif value < input_array[index]:
                upper_index = index
            elif value > input_array[index]:
                lower_index = index

            if upper_index - lower_index == 1:
                break

            index = (lower_index + upper_index) // 2
        return -1


test_list = [1, 3, 9, 11, 15, 19, 29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))
