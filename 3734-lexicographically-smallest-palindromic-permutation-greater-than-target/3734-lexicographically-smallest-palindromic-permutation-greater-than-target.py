from collections import Counter

class Solution:
    def lexPalindromicPermutation(self,s: str,target: str) -> str:
        count=Counter(s)

        if sum(v%2 for v in count.values())>1:
            return ""

        middle=""
        half_count=Counter()

        for ch,v in count.items():
            half_count[ch]=v//2
            if v%2:
                middle=ch

        n=len(s)
        half_len=n//2
        target_half=target[:half_len]

        rem=half_count.copy()

        for ch in target_half:
            rem[ch]-=1
            if rem[ch]<0:
                break
        else:
            half=target_half
            candidate=half+middle+half[::-1]

            if candidate>target:
                return candidate

        rem=half_count.copy()
        states=[]

        for i in range(half_len):
            states.append(rem.copy())

            ch=target_half[i]
            rem[ch]-=1

            if rem[ch]<0:
                break

        for i in range(len(states)-1,-1,-1):
            rem=states[i]
            ch=target_half[i]

            for j in range(ord(ch)+1,ord('z')+1):
                nxt=chr(j)

                if rem[nxt]>0:
                    rem[nxt]-=1

                    suffix=[]

                    for c in range(ord('a'),ord('z')+1):
                        x=chr(c)
                        suffix.append(x*rem[x])

                    half=target_half[:i]+nxt+''.join(suffix)
                    candidate=half+middle+half[::-1]

                    if candidate>target:
                        return candidate

                    rem[nxt]+=1

        return ""