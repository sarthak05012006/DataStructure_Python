def binary_seatch(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right :
        middle = (left+right)//2

        if nums[middle] == target:
            return middle
        elif nums[middle] < target:
            left = middle + 1 
        else:
            right = middle - 1
    return -1

nums = [12,25,34,45,56,78,89]
print(binary_seatch(nums,56))