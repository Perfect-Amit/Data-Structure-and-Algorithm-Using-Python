class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n=len(num)
        for i in range(1,n):
            for j in range(i+1,n):
                a=num[:i]
                b=num[i:j]
                if len(a)>1 and a[0]=='0':
                    break
                if len(b)>1 and b[0]=='0':
                    break
                while j<n:
                    total=str(int(a)+int(b))
                    if not num.startswith(total,j):
                        break
                    j+=len(total)
                    a,b=b,total
                    if j==n:
                        return True
        return False