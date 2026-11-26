class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        elif n == 10:
            return True
        elif n > 10 and n < 19:
            return True
        elif n == 19:
            return False
        elif n > 19 and n < 27:
            return False
        elif n == 27:
            return True
        elif n > 27 and n < 34:
            return True
        elif n == 34:
            return False
        elif n > 34 and n < 40:
            return False
        elif n == 40:
            return True
        elif n > 40 and n < 45:
            return True
        elif n == 45:
            return False
        elif n > 45 and n < 49:
            return False
        else:
            return True