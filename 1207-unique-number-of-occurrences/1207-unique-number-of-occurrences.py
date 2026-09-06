from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        s_arr=set(arr)
        s_list = list(s_arr)
        for i in range(len(s_list)):
            for j in range(i+1, len(s_list)):
                if count[s_list[i]] == count[s_list[j]]:
                    return False
        return True