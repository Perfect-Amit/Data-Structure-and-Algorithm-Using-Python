class Solution:
    def reverseDegree(self, s: str) -> int:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        nums = [26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        k = 1
        x = 0
        res = 0
        for ch in s:
            if ch in alpha:
                x = alpha.index(ch)
                res += nums[x] * k
            k += 1
            x = 0
        return res