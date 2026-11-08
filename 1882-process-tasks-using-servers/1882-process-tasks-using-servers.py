import heapq
class Solution:
    def assignTasks(self,servers: list[int],tasks: list[int]) -> list[int]:
        available=[]
        busy=[]
        for i,w in enumerate(servers):
            heapq.heappush(available,(w,i))
        res=[0]*len(tasks)
        time=0
        for i,duration in enumerate(tasks):
            time=max(time,i)
            while busy and busy[0][0]<=time:
                free,w,idx=heapq.heappop(busy)
                heapq.heappush(available,(w,idx))
            if not available:
                time=busy[0][0]
                while busy and busy[0][0]<=time:
                    free,w,idx=heapq.heappop(busy)
                    heapq.heappush(available,(w,idx))
            w,idx=heapq.heappop(available)
            res[i]=idx
            heapq.heappush(busy,(time+duration,w,idx))
        return res