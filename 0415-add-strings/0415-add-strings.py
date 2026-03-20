class Solution:
    def addStrings(self, num1, num2):
        i=len(num1)-1
        j=len(num2)-1
        carry=0
        res=[]

        while i>=0 or j>=0 or carry:
            d1=ord(num1[i])-48 if i>=0 else 0
            d2=ord(num2[j])-48 if j>=0 else 0

            total=d1+d2+carry
            res.append(str(total%10))
            carry=total//10

            i-=1
            j-=1

        return ''.join(res[::-1])