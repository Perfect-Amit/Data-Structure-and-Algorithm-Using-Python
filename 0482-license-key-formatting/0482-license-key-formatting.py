class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s=s.replace('-','').upper()
        first=len(s)%k
        if first==0:
            first=k
        ans=s[:first]
        for i in range(first,len(s),k):
            ans+='-'+s[i:i+k]
        return ans