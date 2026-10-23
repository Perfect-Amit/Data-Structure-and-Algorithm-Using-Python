class Solution:
    def arrayNesting(self,nums:list[int])->int:
        n=len(nums)
        visited=[False]*n
        res=0
        for i in range(n):
            if visited[i]:
                continue
            count=0
            k=i
            while not visited[k]:
                visited[k]=True
                count+=1
                k=nums[k]
            res=max(res,count)
        return res