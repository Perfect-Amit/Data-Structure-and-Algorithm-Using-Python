class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        ans=""
        for word in words:
            total=0
            for ch in word:
                index=alpha.index(ch)
                total+=weights[index]
            value=total%26
            ans+=alpha[25-value]
        return ans