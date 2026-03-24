class Solution:
    def decrypt(self, code, k):
        n=len(code)
        res=[0]*n
        
        if k==0:
            return res
        
        code=code+code
        
        if k>0:
            window=sum(code[1:k+1])
            for i in range(n):
                res[i]=window
                window+=code[i+k+1]-code[i+1]
        else:
            k=-k
            window=sum(code[n-k:n])
            for i in range(n):
                res[i]=window
                window+=code[i+n]-code[i+n-k]
        
        return res