# You are climbing a stair case. It takes n steps to reach to the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Note: Given n will be a positive integer.

# Example 1:

# Input: 3
# Output: 3



def climbingSteps(n):
    if n == 1: return 1
    if n == 2: return 2

    twoAway = 1
    oneAway = 2

    for i in range(3, n + 1):
        current = twoAway + oneAway
        twoAway = oneAway
        oneAway = current 
    
    return current

