def bubble_sort(nums):
    n = len(nums) 
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums
nums = [19,11,12,15,21,9,8,3,2]
print(bubble_sort(nums))
print(len(nums))