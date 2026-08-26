class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for ch in word:
            freq[ch] = freq.get(ch, 0) + 1
        counts = sorted(freq.values(), reverse=True)
        return sum(freq * (i // 8 + 1) for i, freq in enumerate(counts))