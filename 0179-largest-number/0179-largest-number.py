from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        nums=list(map(str,nums))

        def cmp(a,b):
            if a+b>b+a:
                return -1
            elif a+b<b+a:
                return 1
            return 0

        nums.sort(key=cmp_to_key(cmp))

        res=''.join(nums)

        if res[0]=='0':
            return "0"

        return res