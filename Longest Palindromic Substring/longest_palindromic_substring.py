class Solution:
    def expand(self, l, r, s):
        while (l >= 0 and r < len(s) and (s[l] == s[r])):
            l -= 1
            r += 1
        return s[l+1:r]

    def longestPalindrome(self, s: str) -> str:
        result = ''
        for i in range(len(s)):
            sub1 = self.expand(i, i, s)
            if len(sub1) > len(result): result = sub1
            sub2 = self.expand(i, i+1, s)
            if len(sub2) > len(result): result = sub2
        return result