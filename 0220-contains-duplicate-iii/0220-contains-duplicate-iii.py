class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        if valueDiff<0:
            return False

        bucket={}
        size=valueDiff+1

        for i,num in enumerate(nums):
            bid=num//size

            if bid in bucket:
                return True

            if bid-1 in bucket and abs(num-bucket[bid-1])<=valueDiff:
                return True

            if bid+1 in bucket and abs(num-bucket[bid+1])<=valueDiff:
                return True

            bucket[bid]=num

            if i>=indexDiff:
                old=nums[i-indexDiff]
                del bucket[old//size]

        return False