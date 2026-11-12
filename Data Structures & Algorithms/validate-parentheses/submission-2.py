class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        
        for i in range(len(s)):
            if s[i] not in pairs:
                stack.append(s[i])
            else:
                if not stack:
                    return False
                rem = stack.pop()
                if rem != pairs[s[i]]:
                    return False
        
        if stack:
            return False
        
        return True
