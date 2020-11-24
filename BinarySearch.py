def binarySearch(arr, elem):
    i = 0
    j = len(arr) - 1
    while i <= j:
        mid = i + (j - i) // 2
        if elem == arr[mid]:
            return mid
        if elem < arr[mid]:
            j = mid - 1
        if elem > arr[mid]:
            i = mid + 1
    return -1
