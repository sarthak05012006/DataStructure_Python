def count_frequency(arr):
    freq_map = {}
    for item in arr:
        # If item exists, increment it; otherwise, initialize it to 0 and add 1
        freq_map[item] = freq_map.get(item, 0) + 1
    return freq_map

fruits = ["apple", "banana", "apple", "cherry", "banana", "apple"]
print(count_frequency(fruits))  