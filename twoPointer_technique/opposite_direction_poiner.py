def two_sum_sorted(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [numbers[left], numbers[right]] # Found the indices
        elif current_sum < target:
            left += 1  # Need a larger sum, move left pointer forward
        else:
            right -= 1 # Need a smaller sum, move right pointer backward
            
    return [] # No pair found
numbers = [1,3,5,6,8,11]
print(two_sum_sorted(numbers,4))