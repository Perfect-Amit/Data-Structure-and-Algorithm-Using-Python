class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp=[0]*k
        ans=[0]*k
        for num in nums:
            new=[0]*k
            r=num%k
            new[r]+=1
            for j in range(k):
                if dp[j]:
                    new[(j*r)%k]+=dp[j]
            for j in range(k):
                ans[j]+=new[j]
            dp=new
        return ans