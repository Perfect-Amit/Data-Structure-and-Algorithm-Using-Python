from collections import defaultdict
class Solution:
    def palindromePath(self,n:int,edges:list[list[int]],s:str,queries:list[str])->list[bool]:
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        parent=[-1]*n
        depth=[0]*n
        size=[1]*n
        heavy=[-1]*n
        order=[0]
        for u in order:
            for v in g[u]:
                if v==parent[u]:
                    continue
                parent[v]=u
                depth[v]=depth[u]+1
                order.append(v)
        for u in order[::-1]:
            best=0
            for v in g[u]:
                if parent[v]==u:
                    size[u]+=size[v]
                    if size[v]>best:
                        best=size[v]
                        heavy[u]=v
        head=[0]*n
        pos=[0]*n
        timer=0
        stack=[(0,0)]
        while stack:
            u,h=stack.pop()
            while u!=-1:
                head[u]=h
                pos[u]=timer
                timer+=1
                for v in g[u]:
                    if parent[v]==u and v!=heavy[u]:
                        stack.append((v,v))
                u=heavy[u]
        seg=[0]*(2*n)
        for u in range(n):
            seg[n+pos[u]]=1<<(ord(s[u])-97)
        for i in range(n-1,0,-1):
            seg[i]=seg[2*i]^seg[2*i+1]
        def update(p,val):
            p+=n
            seg[p]=val
            p//=2
            while p:
                seg[p]=seg[2*p]^seg[2*p+1]
                p//=2
        def range_xor(l,r):
            l+=n
            r+=n+1
            ans=0
            while l<r:
                if l&1:
                    ans^=seg[l]
                    l+=1
                if r&1:
                    r-=1
                    ans^=seg[r]
                l//=2
                r//=2
            return ans
        def path_xor(u,v):
            ans=0
            while head[u]!=head[v]:
                if depth[head[u]]<depth[head[v]]:
                    u,v=v,u
                ans^=range_xor(pos[head[u]],pos[u])
                u=parent[head[u]]
            if depth[u]>depth[v]:
                u,v=v,u
            ans^=range_xor(pos[u],pos[v])
            return ans
        ans=[]
        chars=list(s)
        for q in queries:
            parts=q.split()
            if parts[0]=="update":
                u=int(parts[1])
                c=parts[2]
                chars[u]=c
                update(pos[u],1<<(ord(c)-97))
            else:
                u,v=int(parts[1]),int(parts[2])
                mask=path_xor(u,v)
                ans.append(mask==0 or (mask&(mask-1))==0)
        return ans