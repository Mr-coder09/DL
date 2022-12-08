#selection sort
def selectionSort(array, size):
       for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        (array[step], array[min_idx]) = (array[min_idx], array[step])
data = [-8 ,-7 ,0 ,-7 ,-9 ,10 ,200, 100]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
for k in range(7,2,-1):
    print(data[k])
#bubble sort
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]                     #algoritham and output write on assignment pages
                if not swapped:
                    return
arr = [64, 34, 25, 12, 22, 11, 90]
print("The unsorted array is:",arr)
bubbleSort(arr)
print("Sorted array is:")
for i in range(6,1,-1):
    print(arr[i],end="  ")
