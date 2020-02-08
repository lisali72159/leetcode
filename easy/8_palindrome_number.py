# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

 def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        num = 0
        temp = x
        while temp:
            last_digit = temp % 10
            num = (num * 10 + last_digit)
            temp = temp // 10
        return num == x