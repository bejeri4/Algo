def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def part(arr, l, r):
    p = r
    while True:
        while arr[l] <= arr[p] and l < r:
            l += 1
        while arr[r] >= arr[p] and l < r:
            r -= 1
        if l == r:
            break
        swap(arr, l, r)
    swap(arr, r, p)
    return r

            
            
def quickSort(arr, l, r):
    if l < r:
        p = part(arr, l, r)
        quickSort(arr, l, p - 1)
        quickSort(arr, p + 1, r)
