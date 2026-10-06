class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly=[1]
        i2=i3=i5=0
        for _ in range(1,n):
            a=ugly[i2]*2
            b=ugly[i3]*3
            c=ugly[i5]*5
            next_num=min(a,b,c)
            ugly.append(next_num)
            if next_num==a:
                i2+=1
            if next_num==b:
                i3+=1
            if next_num==c:
                i5+=1
        return ugly[-1]