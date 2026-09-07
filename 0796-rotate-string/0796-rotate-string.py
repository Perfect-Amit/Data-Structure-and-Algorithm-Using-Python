class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a = ''
        b = ''
        for i in range(len(s)):
            a = s[1:len(s)]
            b = a+s[0]
            s = b
            if s == goal:
                return True
        return False