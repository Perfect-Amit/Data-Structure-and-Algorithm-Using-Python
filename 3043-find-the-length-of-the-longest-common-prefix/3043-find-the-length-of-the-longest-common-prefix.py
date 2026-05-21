class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        st = set()
        for x in arr1:
            s = str(x)
            for i in range(1, len(s) + 1):
                st.add(s[:i])
        ans = 0
        for x in arr2:
            s = str(x)
            for i in range(1, len(s) + 1):
                if s[:i] in st:
                    ans = max(ans, i)
        return ans