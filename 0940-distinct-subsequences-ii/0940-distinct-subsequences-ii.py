from itertools import combinations
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        last_seen_contribution = {}
        current_total = 0
        for char in s:
            new_subsequences = (current_total + 1) % mod
            old_contribution = last_seen_contribution.get(char, 0)
            current_total = (current_total + new_subsequences - old_contribution) % mod
            last_seen_contribution[char] = new_subsequences
        return current_total % mod