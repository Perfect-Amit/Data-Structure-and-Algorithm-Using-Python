import collections

DIGIT_FACTORS = {
    0: collections.Counter(), 1: collections.Counter(),
    2: collections.Counter([2]), 3: collections.Counter([3]),
    4: collections.Counter([2, 2]), 5: collections.Counter([5]),
    6: collections.Counter([2, 3]), 7: collections.Counter([7]),
    8: collections.Counter([2, 2, 2]), 9: collections.Counter([3, 3]),
}

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        need, ok = self._factorize(t)
        if not ok:
            return "-1"

        minimalDigits = self._toDigits(need)
        if sum(minimalDigits.values()) > len(num):
            return self._build(minimalDigits)

        have = sum((DIGIT_FACTORS[int(c)] for c in num), collections.Counter())

        firstZero = next((i for i, c in enumerate(num) if c == '0'), len(num))
        if firstZero == len(num) and all(have[p] >= need[p] for p in need):
            return num

        for i in range(len(num) - 1, -1, -1):
            d = int(num[i])
            have -= DIGIT_FACTORS[d]
            spaceLeft = len(num) - 1 - i

            if i > firstZero:
                continue

            for bigger in range(d + 1, 10):
                remaining = need - have - DIGIT_FACTORS[bigger]
                for p in list(remaining):
                    if remaining[p] < 0:
                        remaining[p] = 0
                fillDigits = self._toDigits(remaining)
                needed = sum(fillDigits.values())
                if needed <= spaceLeft:
                    ones = spaceLeft - needed
                    return (num[:i] + str(bigger) + '1' * ones +
                            self._build(fillDigits))

        digits = self._toDigits(need)
        onesCount = len(num) + 1 - sum(digits.values())
        return '1' * onesCount + self._build(digits)

    def _factorize(self, t: int):
        count = collections.Counter({2: 0, 3: 0, 5: 0, 7: 0})
        for p in (2, 3, 5, 7):
            while t % p == 0:
                t //= p
                count[p] += 1
        return count, t == 1

    def _toDigits(self, count: collections.Counter) -> collections.Counter:
        c = collections.Counter(count)
        c8, rem2 = divmod(c[2], 3)
        c9, c3 = divmod(c[3], 2)
        c4, c2 = divmod(rem2, 2)
        if c2 == 1 and c3 == 1:
            c2, c3, c6 = 0, 0, 1
        else:
            c6 = 0
        if c3 == 1 and c4 == 1:
            c2, c6, c3, c4 = 1, 1, 0, 0
        return collections.Counter({2: c2, 3: c3, 4: c4, 5: c[5],
                                     6: c6, 7: c[7], 8: c8, 9: c9})

    def _build(self, digitCounts: collections.Counter) -> str:
        return ''.join(str(d) * digitCounts[d] for d in range(2, 10))