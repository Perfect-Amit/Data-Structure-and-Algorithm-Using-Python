class Solution:
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        def possible(time):
            total=0
            for t in workerTimes:
                left,right=0,mountainHeight
                while left<=right:
                    mid=(left+right)//2
                    if t*mid*(mid+1)//2<=time:
                        left=mid+1
                    else:
                        right=mid-1
                total+=right
                if total>=mountainHeight:
                    return True
            return False

        left,right=0,10**18
        ans=right
        while left<=right:
            mid=(left+right)//2
            if possible(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans