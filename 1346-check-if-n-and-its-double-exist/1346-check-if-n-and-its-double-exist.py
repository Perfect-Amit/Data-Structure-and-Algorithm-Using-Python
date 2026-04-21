class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] == 0 and arr[j] == 0 and i == j:
                    continue
                elif arr[j]*2 != arr[i]:
                    continue
                else:
                    return True
        return False