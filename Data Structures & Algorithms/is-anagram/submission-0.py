class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        return self.helper(s) == self.helper(t)
    
    def helper(self, s):
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1

        return count