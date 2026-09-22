class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        res=[]
        def backtrack(index,path,value,prev):
            if index==len(num):
                if value==target:
                    res.append(path)
                return
            for j in range(index,len(num)):
                if j>index and num[index]=='0':
                    break
                cur=int(num[index:j+1])
                if index==0:
                    backtrack(j+1,str(cur),cur,cur)
                else:
                    backtrack(j+1,path+'+'+str(cur),value+cur,cur)
                    backtrack(j+1,path+'-'+str(cur),value-cur,-cur)
                    backtrack(j+1,path+'*'+str(cur),value-prev+prev*cur,prev*cur)
        backtrack(0,'',0,0)
        return res