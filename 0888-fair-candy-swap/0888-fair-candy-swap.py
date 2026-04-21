class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        A = sum(aliceSizes)
        B = sum(bobSizes)
        diff = (A - B) // 2
        st = set(bobSizes)
        for x in aliceSizes:
            if x - diff in st:
                return [x, x - diff]