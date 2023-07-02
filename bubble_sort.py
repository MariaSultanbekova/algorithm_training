def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):  # постепенно уходим от конца, там всплывают бОльшие элементы
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr


print(bubble_sort([4, 2, 3, 1, 0, 5, 8, 9, 50000, 1000]))

# [0, 1, 2, 3, 4, 5, 8, 9, 1000, 50000]
