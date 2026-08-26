def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if nums[j] < nums[min_index]:
                min_index = j
        temp = nums[i]
        nums[i] = nums[min_index]
        nums[min_index] = temp
    
    return nums

nums = [90,84,87,10,9,32]
print(selection_sort(nums))