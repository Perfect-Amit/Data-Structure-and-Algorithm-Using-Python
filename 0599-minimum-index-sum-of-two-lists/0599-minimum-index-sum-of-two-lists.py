class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mp = {}
        for i in range(len(list2)):
            mp[list2[i]] = i
        ans = []
        minSum = float('inf')
        for i in range(len(list1)):
            if list1[i] in mp:
                temp_sum = i + mp[list1[i]]
                if temp_sum < minSum:
                    minSum = temp_sum
                    ans = [list1[i]]
                elif temp_sum == minSum:
                    ans.append(list1[i])
        return ans
