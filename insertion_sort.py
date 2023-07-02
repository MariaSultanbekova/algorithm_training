def insertion_sort(arr):  # // F.C.
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]  # двигаем элементы вперед, потому что они больше key
            j -= 1

        arr[j+1] = key  # key занимает свое место, после того как все подвинулись

    return arr


print(insertion_sort([4, 2, 1, 3, 5, 7]))

# [1, 2, 3, 4, 5, 7]
