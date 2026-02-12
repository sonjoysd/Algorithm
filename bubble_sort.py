def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>= arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr



arr = [10,12,20,40,8,100]
print(bubble_sort(arr))
