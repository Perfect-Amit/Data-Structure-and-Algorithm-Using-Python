import heapq
class Solution:
    def busiestServers(self,k: int,arrival: list[int],load: list[int]) -> list[int]:
        size=1
        while size<k:
            size*=2
        tree=[0]*(2*size)
        for i in range(k):
            tree[size+i]=1
        for i in range(size-1,0,-1):
            tree[i]=tree[2*i]+tree[2*i+1]
        def update(idx,val):
            idx+=size
            tree[idx]=val
            while idx>1:
                idx//=2
                tree[idx]=tree[2*idx]+tree[2*idx+1]
        def find(node,left,right,start):
            if right<start or tree[node]==0:
                return -1
            if left==right:
                return left
            mid=(left+right)//2
            res=find(node*2,left,mid,start)
            if res!=-1:
                return res
            return find(node*2+1,mid+1,right,start)
        busy=[]
        count=[0]*k
        for i in range(len(arrival)):
            time=arrival[i]
            while busy and busy[0][0]<=time:
                finish,server=heapq.heappop(busy)
                update(server,1)
            preferred=i%k
            server=find(1,0,size-1,preferred)
            if server==-1:
                server=find(1,0,size-1,0)
            if server==-1:
                continue
            update(server,0)
            count[server]+=1
            heapq.heappush(
                busy,
                (time+load[i],server)
            )
        maximum=max(count)
        return [i for i in range(k) if count[i]==maximum]