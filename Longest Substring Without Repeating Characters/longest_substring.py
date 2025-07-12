class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0: return 0
        elif len(s) == 1: return 1
        elif len(set(s)) == 1: return 1
        aux = ''
        max_length  = 0
        for character in s:
            if character in aux:

                aux = aux[aux.index(character)+1:]
            aux += character
            max_length = max(max_length, len(aux))
        return max_length


