# Max subarray

# Input:[-2,1,-3,4,-1,2,1,-5,4], 4

# Output: 6 [4,-1,2,1] has the largest sum = 6

# Find contiguous subarray that gives maximum sum (at least 1 number) and return its sum.


def max_sum(arr):
    current_max = arr[0]
    max_sum = current_max
    for num in nums[1:]:
        current_max = max(hum, current_max + num)
        max_sum = max(current_max, max_sum)
    return max_sum


#  Iterate through the array. Track current sum as first number in the array. Compare arr[i] and arr[i + 1]. If the sum is greater than the element alone, add to the sum. If the next ele is greater than the current sum, then new max sum is just the new ele. 
