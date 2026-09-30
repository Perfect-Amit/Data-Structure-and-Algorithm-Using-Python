class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        arr = list(set(word))
        res = 0
        for i in range(len(arr)):
            if arr[i].upper() != arr[i] and arr[i].upper() in arr:
                res += 1
        return res