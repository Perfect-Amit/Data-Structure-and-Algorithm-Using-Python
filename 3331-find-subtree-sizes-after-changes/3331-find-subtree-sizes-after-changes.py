class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n=len(parent)
        adj=[[] for _ in range(n)]

        for i in range(1,n):
            adj[parent[i]].append(i)

        new_parent=parent[:]
        last={}
        stack=[(0,0,-1)]

        while stack:
            node,state,old=stack.pop()
            c=s[node]

            if state==0:
                prev=last.get(c,-1)

                if prev!=-1:
                    new_parent[node]=prev

                last[c]=node
                stack.append((node,1,prev))

                for child in reversed(adj[node]):
                    stack.append((child,0,-1))
            else:
                if old==-1:
                    last.pop(c,None)
                else:
                    last[c]=old

        tree=[[] for _ in range(n)]

        for i in range(1,n):
            tree[new_parent[i]].append(i)

        ans=[1]*n
        order=[0]
        traversal=[]
        while order:
            node=order.pop()
            traversal.append(node)
            for child in tree[node]:
                order.append(child)
        for node in reversed(traversal[1:]):
            ans[new_parent[node]]+=ans[node]
        return ans