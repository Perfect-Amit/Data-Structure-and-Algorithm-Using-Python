class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        count=Counter(s)
        for i,ch in enumerate(s):
            if count[ch]<k:
                left=self.longestSubstring(s[:i],k)
                right=self.longestSubstring(s[i+1:],k)
                return max(left,right)
        return len(s)