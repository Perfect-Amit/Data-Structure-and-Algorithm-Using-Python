class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for x in operations:
            if x == '+':
                st.append(st[-1] + st[-2])
            elif x == 'D':
                st.append(2 * st[-1])
            elif x == 'C':
                st.pop()
            else:
                st.append(int(x))
        return sum(st)