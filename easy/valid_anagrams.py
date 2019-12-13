# Valid anagrams: Check if two strings are anagrams 
  
  def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        dictionary = {}
        
        for i in range(len(s)):
            if s[i] not in dictionary:
                dictionary[s[i]] = 1
            else:
                dictionary[s[i]] += 1
                
        for j in range(len(t)):
            if t[j] in dictionary:
                dictionary[t[j]] -= 1
            else:
                return False
        
        return all(value == 0 for value in dictionary.values())