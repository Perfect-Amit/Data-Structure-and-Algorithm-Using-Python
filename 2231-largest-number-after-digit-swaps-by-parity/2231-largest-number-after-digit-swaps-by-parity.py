class Solution:
    def largestInteger(self, num: int) -> int:
        digits=list(str(num))
        for i in range(len(digits)):
            best=i
            for j in range(i+1,len(digits)):
                if int(digits[j])%2==int(digits[i])%2 and digits[j]>digits[best]:
                    best=j
            digits[i],digits[best]=digits[best],digits[i]
        return int(''.join(digits))