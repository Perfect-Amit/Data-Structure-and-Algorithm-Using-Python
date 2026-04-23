class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        num = False
        dot = False
        exp = False
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = True
            elif c in '+-':
                if i > 0 and s[i-1] not in 'eE':
                    return False
            elif c == '.':
                if dot or exp:
                    return False
                dot = True
            elif c in 'eE':
                if exp or not num:
                    return False
                exp = True
                num = False
            else:
                return False
        return num