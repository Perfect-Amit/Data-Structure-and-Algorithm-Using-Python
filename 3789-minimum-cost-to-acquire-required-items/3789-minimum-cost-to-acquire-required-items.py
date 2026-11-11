class Solution:
    def minimumCost(self,cost1: int,cost2: int,costBoth: int,need1: int,need2: int) -> int:
        common=min(need1,need2)
        remaining1=max(0,need1-need2)
        remaining2=max(0,need2-need1)
        res=common*min(costBoth,cost1+cost2)
        res+=remaining1*min(cost1,costBoth)
        res+=remaining2*min(cost2,costBoth)
        return res