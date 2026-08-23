class Solution:
    def checkDivisibility(self, n: int) -> bool:
        res = False
        Sum = 0
        Prod = 1
        x = n
        while n != 0:
            Sum += n%10
            Prod *= n%10
            n = n//10
        if x % (Sum+Prod) == 0:
            res = True
        return res