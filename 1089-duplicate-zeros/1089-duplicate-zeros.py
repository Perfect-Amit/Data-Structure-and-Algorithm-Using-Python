class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        arr2 = []
        n = len(arr)
        for i in range(n):
            if arr[i] == 0:
                arr2.append(0)
                arr2.append(0)
            else:
                arr2.append(arr[i])
        arr[:] = arr2[:n]