# Merge Sort Alorithm
# Takes the array and splits into half
# Recursively calls itself until the array is of size 1
# Then merges the arrays back together in sorted order
# Time Complexity: O(nlogn)

# Algorithm
# 1. Split the array into two halves

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])

            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining elements from both halves
    
    result.extend(left[left_index:])
    result.extend(right[right_index:])
    return result

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
