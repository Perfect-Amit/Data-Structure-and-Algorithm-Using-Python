class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        arr=sorted((value,index) for index,value in enumerate(nums))
        ans=nums[:]

        i=0

        while i<len(arr):
            j=i

            while j+1<len(arr) and arr[j+1][0]-arr[j][0]<=limit:
                j+=1

            values=sorted(x[0] for x in arr[i:j+1])
            indices=sorted(x[1] for x in arr[i:j+1])

            for index,value in zip(indices,values):
                ans[index]=value

            i=j+1

        return ans