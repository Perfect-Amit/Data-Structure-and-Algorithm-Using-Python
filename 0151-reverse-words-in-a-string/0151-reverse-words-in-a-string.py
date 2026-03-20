class Solution:
    def reverseWords(self, s):
        arr=s.split()
        arr=arr[::-1]
        return " ".join(arr)