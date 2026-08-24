class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in invocations:
            graph[a].append(b)
        suspicious = set()
        stack = [k]
        while stack:
            node = stack.pop()
            if node in suspicious:
                continue
            suspicious.add(node)
            for nxt in graph[node]:
                stack.append(nxt)
        for a, b in invocations:
            if a not in suspicious and b in suspicious:
                return list(range(n))
        return [i for i in range(n) if i not in suspicious]