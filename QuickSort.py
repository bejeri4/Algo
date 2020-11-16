def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


def partition(arr, l, r):
    # Uncoment next line if you would like to choose mid element as a pivot
    # swap(arr, l + (r - l) // 2, r)
    p = r
    while True:
        while l < r and arr[l] <= arr[p]:
            l += 1
        while l < r and arr[r] >= arr[p]:
            r -= 1
        if l == r:
            break
        swap(arr, l, r)
    swap(arr, r, p)
    return r

def quickSort(arr, l, r):
    if l < r:
        p = partition(arr, l, r)
        quickSort(arr, l, p - 1)
        quickSort(arr, p + 1, r)
