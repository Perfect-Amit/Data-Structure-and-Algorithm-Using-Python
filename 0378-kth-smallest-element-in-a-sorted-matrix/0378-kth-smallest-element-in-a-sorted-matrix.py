class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        flat_list = sum(matrix, [])
        flat_list.sort()
        return flat_list[k-1]