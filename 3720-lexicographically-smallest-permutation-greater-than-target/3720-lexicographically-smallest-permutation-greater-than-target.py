class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for ch in target:
            count[ord(ch) - ord('a')] -= 1

        for i in range(len(s) - 1, -1, -1):
            cur = ord(target[i]) - ord('a')
            count[cur] += 1

            if any(x < 0 for x in count):
                continue

            for j in range(cur + 1, 26):
                if count[j] > 0:
                    count[j] -= 1

                    ans = target[:i] + chr(j + ord('a'))

                    for x in range(26):
                        ans += chr(x + ord('a')) * count[x]

                    return ans

        return ""