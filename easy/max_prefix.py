  def longestCommonPrefix(self, strs: List[str]) -> str:
        minimum = float("inf")
        smallest_word = None
        for word in strs:
            if len(word) < minimum:
                minimum = len(word)
                smallest_word = word

        i = 0
        while i < minimum:
            for word in strs:
                if smallest_word[i] != word[i]:
                    return smallest_word[0:i]
            i += 1
        return smallest_word