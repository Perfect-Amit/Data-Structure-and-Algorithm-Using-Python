from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = paragraph.lower()
        clean = ""
        for ch in paragraph:
            if ch.isalnum():
                clean += ch
            else:
                clean += " "
        words = clean.split()
        banned=set(banned)
        count=Counter(words)
        res=""
        max_freq=0
        for word in count:
            if word not in banned and count[word]>max_freq:
                res=word
                max_freq=count[word]
        return res