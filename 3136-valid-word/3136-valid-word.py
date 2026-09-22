class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if not word.isalnum():
            return False
        vowel=False
        consonant=False
        for ch in word:
            if ch.lower() in "aeiou":
                vowel=True
            elif ch.isalpha():
                consonant=True
        return vowel and consonant