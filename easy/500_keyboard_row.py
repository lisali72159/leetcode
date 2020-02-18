# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]

def findWords(words):
    list1 = set('qwertyuiop')
    list2 = set('asdfghjkl')
    list3 = set('zxcvbnm')
    result = []
    for word in words:
        new_list = set(word.lower())
        if new_list <= list1 or new_list <= list2 or new_list <= list3:
            result.append(word)

    return result