def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):

        # Assume current index has minimum
        min_index = i

        # Find smallest element
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap elements
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Main
arr = [64, 25, 12, 22, 11]

print("Original Array:")
print(arr)

selection_sort(arr)

print("Sorted Array:")
print(arr)