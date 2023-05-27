"""
Implement quick sort in Python.
Input a list.
Output a sorted list.
"""


def quicksort(array: list) -> list:
    if len(array) == 1:
        return array
    # pivot element is usually the last one in the array
    pivot = array[-1]

    # each each of the element in the array
    for i in range(len(array) - 1):
        # while the first is > pivot
        while array[i] > pivot:
            # break if the index of element being compared = index of pivot
            if i == array.index(pivot):
                break
            # print(array)
            # move it to the right of pivot
            # and move the preceding element to the first position
            pivot_index = array.index(pivot)
            prev_index = pivot_index - 1

            array[pivot_index] = array[i]
            temp = array[prev_index]
            array[i] = temp
            array[prev_index] = pivot
        # no need to process the remaining elements
        if i == array.index(pivot):
                break
    
    left_array = array[:array.index(pivot)]
    # sort only if there are at leaset 2 elements
    if len(left_array) > 1:
        # print(f"left {left_array}")
        left_array = quicksort(left_array)

    right_array = array[array.index(pivot) + 1:]
    # sort only if there are at leaset 2 elements
    if len(right_array) > 1:
        # print(f"right {right_array}")
        right_array = quicksort(right_array)

    # join sorted arrays around pivot
    array = left_array + [pivot] + right_array
    
    return array


test: list = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
# test: list = [8, 2, 9, 1, 5]
print(quicksort(test))
