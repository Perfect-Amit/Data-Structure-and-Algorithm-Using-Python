class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        limit=1000001
        freq=[0]*26
        for ch in s:
            freq[ord(ch)-97]+=1
        mid=''
        for i in range(26):
            if freq[i]%2:
                mid=chr(i+97)
                break
        half=[x//2 for x in freq]
        half_len=sum(half)
        def count_permutations(counts):
            remaining=sum(counts)
            result=1
            for count in counts:
                if count==0:
                    continue
                choose=min(count,remaining-count)
                ways=1
                for i in range(1,choose+1):
                    ways=ways*(remaining-i+1)//i
                    if ways>=limit:
                        ways=limit
                        break
                result*=ways
                if result>=limit:
                    return limit
                remaining-=count
            return result
        if k>count_permutations(half):
            return ''
        left=[]
        for _ in range(half_len):
            for i in range(26):
                if half[i]==0:
                    continue
                half[i]-=1
                ways=count_permutations(half)
                if ways>=k:
                    left.append(chr(i+97))
                    break
                k-=ways
                half[i]+=1
        left=''.join(left)
        return left+mid+left[::-1]