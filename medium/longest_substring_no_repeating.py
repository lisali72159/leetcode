# Longest Substring w/o Repeating Characters

def longest(s):
    current = ""
    longest = 0

    for i in range(len(s)):
        if s[i] in current:
            start = current.index(s[i])
            current = current[start] + s[i]
        else:
            current += s[i]
        longest = max(len(current), longest)
    return longest