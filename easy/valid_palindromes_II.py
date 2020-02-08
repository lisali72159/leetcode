#  Are two strings palindromes (allowed to delete one character)?
 
 
 
 
 def validPalindrome(self, s: str) -> bool:
        start_idx = 0
        end_idx = len(s) - 1
        
        while start_idx <= end_idx:
            if s[start_idx] != s[end_idx]:
                s1 = s[start_idx: end_idx]
                s2 = s[start_idx + 1: end_idx + 1]
                return s1 == s1[:: -1] or s2 == s2[:: -1]
            start_idx += 1
            end_idx -=1
        return True