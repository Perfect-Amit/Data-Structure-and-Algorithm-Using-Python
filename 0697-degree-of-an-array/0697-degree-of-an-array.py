class Solution:
    def findShortestSubArray(self, nums):
        freq={}
        first={}
        
        max_freq=0
        min_len=len(nums)
        
        for i,num in enumerate(nums):
            if num not in first:
                first[num]=i
            
            freq[num]=freq.get(num,0)+1
            
            if freq[num]>max_freq:
                max_freq=freq[num]
                min_len=i-first[num]+1
            elif freq[num]==max_freq:
                min_len=min(min_len, i-first[num]+1)
        
        return min_len