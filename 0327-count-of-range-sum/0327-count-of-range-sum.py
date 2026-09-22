class Solution:
    def countRangeSum(self,nums:list[int],lower:int,upper:int)->int:
        prefix=[0]
        for x in nums:
            prefix.append(prefix[-1]+x)
        def merge_sort(left,right):
            if right-left<=1:
                return 0
            mid=(left+right)//2
            count=merge_sort(left,mid)+merge_sort(mid,right)
            j=k=mid
            for i in range(left,mid):
                while k<right and prefix[k]-prefix[i]<lower:
                    k+=1
                while j<right and prefix[j]-prefix[i]<=upper:
                    j+=1
                count+=j-k
            temp=[]
            i=left
            j=mid
            while i<mid and j<right:
                if prefix[i]<=prefix[j]:
                    temp.append(prefix[i])
                    i+=1
                else:
                    temp.append(prefix[j])
                    j+=1
            temp.extend(prefix[i:mid])
            temp.extend(prefix[j:right])
            prefix[left:right]=temp
            return count
        return merge_sort(0,len(prefix))