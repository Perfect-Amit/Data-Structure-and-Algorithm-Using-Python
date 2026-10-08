class Solution:
    def smallestPalindrome(self, s: str) -> str:
        count=[0]*26

        for ch in s:
            count[ord(ch)-ord('a')]+=1

        left=[]
        for i in range(26):
            left.extend([chr(i+ord('a'))]*(count[i]//2))
        left=''.join(left)
        middle=''
        if len(s)%2:
            for i in range(26):
                if count[i]%2:
                    middle=chr(i+ord('a'))
                    break
        return left+middle+left[::-1]