def numWays(steps, arrLen, pos= 0, memo=None):
    if memo is None: memo = {}
    key = (steps, pos) # use tuple as keys for dictionary
    if key in memo: return memo[key]

    # empty default object for memo

    # negative base case
    # if i is out of bounds, return 0
    if pos < 0 or pos >= arrLen or steps < 0:
        return 0
    if pos == 0 and steps == 0:
        return 1
    
    totalWays = 0
    totalWays += numWays(steps - 1, arrLen, pos - 1, memo) # go left
    totalWays += numWays(steps - 1, arrLen, pos, memo) # stay
    totalWays += numWays(steps - 1, arrLen, pos + 1, memo) # go right
    memo[key] = totalWays
    return totalWays

numWays(3,2) # 4
numWays(0,0) # 1




