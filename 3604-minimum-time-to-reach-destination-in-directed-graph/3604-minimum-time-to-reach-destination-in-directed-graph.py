class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, start, end in edges:
            graph[u].append((v, start, end))
        pq = [(0, 0)]
        visited = set()
        while pq:
            time, node = heapq.heappop(pq)
            if node == n - 1:
                return time
            if node in visited:
                continue
            visited.add(node)
            for nei, start, end in graph[node]:
                if time > end:
                    continue
                next_time = max(time, start) + 1
                heapq.heappush(pq, (next_time, nei))
        return -1