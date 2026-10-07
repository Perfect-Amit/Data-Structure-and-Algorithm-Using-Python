class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_remove=0
        right_remove=0
        for ch in s:
            if ch=='(':
                left_remove+=1
            elif ch==')':
                if left_remove>0:
                    left_remove-=1
                else:
                    right_remove+=1
        res=set()
        def dfs(index,path,balance,left_remove,right_remove):
            if index==len(s):
                if balance==0 and left_remove==0 and right_remove==0:
                    res.add(''.join(path))
                return
            ch=s[index]
            if ch=='(' and left_remove>0:
                dfs(index+1,path,balance,left_remove-1,right_remove)
            if ch==')' and right_remove>0:
                dfs(index+1,path,balance,left_remove,right_remove-1)
            if ch=='(':
                path.append(ch)
                dfs(index+1,path,balance+1,left_remove,right_remove)
                path.pop()
            elif ch==')':
                if balance>0:
                    path.append(ch)
                    dfs(index+1,path,balance-1,left_remove,right_remove)
                    path.pop()
            else:
                path.append(ch)
                dfs(index+1,path,balance,left_remove,right_remove)
                path.pop()
        dfs(0,[],0,left_remove,right_remove)
        return list(res)