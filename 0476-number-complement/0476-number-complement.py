class Solution:
    def findComplement(self, num: int) -> int:
        a=bin(num)[2:]
        temp=[]
        for bit in a:
            if bit=='0':
                temp.append('1')
            else:
                temp.append('0')
        return int(''.join(temp),2)