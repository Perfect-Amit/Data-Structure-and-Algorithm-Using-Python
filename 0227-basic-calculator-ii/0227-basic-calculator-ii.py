class Solution:
    def calculate(self, s: str) -> int:
        st = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                num = num * 10 + int(c)
            if c in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    st.append(num)
                elif sign == '-':
                    st.append(-num)
                elif sign == '*':
                    st.append(st.pop() * num)
                else:
                    st.append(int(st.pop() / num))
                sign = c
                num = 0
        return sum(st)