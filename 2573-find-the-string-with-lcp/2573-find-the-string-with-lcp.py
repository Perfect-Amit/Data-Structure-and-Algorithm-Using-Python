class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n=len(lcp)
        for i in range(n):
            if lcp[i][i]!=n-i:
                return ""
        parent=list(range(n))
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            px,py=find(x),find(y)
            if px!=py:
                parent[py]=px
        for i in range(n):
            for j in range(n):
                if lcp[i][j]>0:
                    union(i,j)
        group={}
        ch=ord('a')
        res=[""]*n
        for i in range(n):
            root=find(i)
            if root not in group:
                if ch>ord('z'):
                    return ""
                group[root]=chr(ch)
                ch+=1
            res[i]=group[root]
        word="".join(res)
        dp=[[0]*n for _ in range(n)]
        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if word[i]==word[j]:
                    dp[i][j]=1+(dp[i+1][j+1] if i+1<n and j+1<n else 0)
        if dp!=lcp:
            return ""
        return word