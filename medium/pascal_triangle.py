# Pascal's Triangle
# Given an input, find array of the nth line of Pascal's triangle.

def generate_pascal(num):
    if num == 0: return [1]
    if num == 1: return [1,1]

    prevRow = generate_pascal(num - 1)
    result = []

    for i in range(len(prevRow - 1))
        result.append(prevRow[i] + prevRow[i + 1])
    
    return [1] + result + [1]