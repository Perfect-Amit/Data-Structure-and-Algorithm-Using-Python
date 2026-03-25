class Solution:
    def nextGreatestLetter(self, letters, target):
        res=[]
        for i in range(len(letters)):
            if letters[i]>target:
                res.append(letters[i])
        res.sort()
        if not res:
            return letters[0]
        else:
            return res[0]