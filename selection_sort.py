def selection_sort(arr):
    n = len(arr)
    for i in range(n):

        idx_min = i
        for j in range(i+1, n):
            if arr[j] < arr[idx_min]:
                idx_min = j

        arr[i], arr[idx_min] = arr[idx_min], arr[i]

    return arr


print(selection_sort([10, 4, 8, 3, 5]))

# [3, 4, 5, 8, 10]
