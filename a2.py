def manual_insert(arr, element, target_index):
    # Append a placeholder to expand the size simulator
    arr.append(None) 
    
    # Shift elements from right to left
    for i in range(len(arr) - 1, target_index, -1):
        arr[i] = arr[i - 1]
        
    # Place the new element into the opened slot
    arr[target_index] = element
    return arr

my_array = [1, 2, 4, 5]
print(manual_insert(my_array, 3, 2))  # Output: [1, 2, 3, 4, 5]


def manual_delete(arr, target_index):
    if target_index >= len(arr) or target_index < 0:
        raise IndexError("Index out of bounds")
        
    # Shift elements from left to right to overwrite the index
    for i in range(target_index, len(arr) - 1):
        arr[i] = arr[i + 1]
        
    # Remove the duplicate trailing item left from shifting
    arr.pop() 
    return arr

my_array1 = [10, 20, 99, 30, 40]
print(manual_delete(my_array1, 2))  # Output: [10, 20, 30, 40]