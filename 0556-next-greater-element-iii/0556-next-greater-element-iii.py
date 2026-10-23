class Solution:
    def nextGreaterElement(self,n:int)->int:
        arr=list(str(n))
        i=len(arr)-2
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
        if i<0:
            return -1
        j=len(arr)-1
        while arr[j]<=arr[i]:
            j-=1
        arr[i],arr[j]=arr[j],arr[i]
        arr[i+1:]=arr[i+1:][::-1]
        ans=int(''.join(arr))
        return ans if ans<2**31 else -1