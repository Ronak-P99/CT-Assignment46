def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr




arr = [1, 3, 2, 9, 4, 11, 6, 8,10]
arr2 = simple_sort(arr)
print(arr2)