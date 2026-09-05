class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            x=str(i)
            valid=True
            for j in x:
                y=int(j)
                if y==0 or i%y!=0:
                    valid=False
                    break
            if valid:
                res.append(i)
        return res