class Solution:
    def buildArray(self, target, n):
        res=[]
        i=0
        
        for num in range(1,n+1):
            if i==len(target):
                break
            
            if num==target[i]:
                res.append("Push")
                i+=1
            else:
                res.append("Push")
                res.append("Pop")
        
        return res