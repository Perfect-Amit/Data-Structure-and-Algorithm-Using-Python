from collections import defaultdict
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)
        for i in range(len(nums)):
            pos[nums[i]].append(i)
        res = [0]*len(nums)
        for v in pos:
            arr = pos[v]
            n = len(arr)
            pref = [0]*n
            pref[0] = arr[0]
            for i in range(1, n):
                pref[i] = pref[i-1] + arr[i]
            for i in range(n):
                idx = arr[i]
                left = idx*i - (pref[i-1] if i > 0 else 0)
                right = (pref[n-1] - pref[i]) - idx*(n-i-1)
                res[idx] = left + right
        return res