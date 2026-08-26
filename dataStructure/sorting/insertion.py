def insertion_sort(arr):
    for i in range(1,len(arr)):
        current = arr[i]
        j = i-1

        while(j>=0) and (arr[j]>current):
            arr[j+1] = arr[j]
            j = j-1

        arr[j+1] = current
    

arr = [7,3,5,2,6]
print(len(arr))
insertion_sort(arr)
print(arr)