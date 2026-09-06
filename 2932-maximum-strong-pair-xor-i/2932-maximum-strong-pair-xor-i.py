class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        n = len(nums)
        pairs = []
        binary_xor = 0
        res = 0
        for i in range(n):
            for j in range(i, n):
                if abs(nums[i]-nums[j]) <= min(nums[i], nums[j]):
                    pairs.append([nums[i], nums[j]])
        for a,b in pairs:
            binary_xor = a ^ b
            res = max(binary_xor, res)
        return res