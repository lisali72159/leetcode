# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

 def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, ele in enumerate(nums):
            diff = target - ele
            if diff in dict:
                return [i, dict[diff]]
            else:
                dict[ele] = i
 