def linear_search(nums,target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
      
    
    return -1
nums = [12,45,78,23,56,89,34]
print(linear_search(nums,56))