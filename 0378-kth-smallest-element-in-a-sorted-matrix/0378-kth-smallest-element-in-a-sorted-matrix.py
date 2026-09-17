class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        flat_list = [element for row in matrix for element in row]
        flat_list.sort()
        return flat_list[k-1]