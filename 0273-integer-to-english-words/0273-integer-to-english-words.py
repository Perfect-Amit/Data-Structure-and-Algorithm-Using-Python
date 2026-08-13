class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        ones = [
            "", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        def under1000(n):
            ans = []
            if n >= 100:
                ans.append(ones[n // 100])
                ans.append("Hundred")
                n %= 100
            if n >= 20:
                ans.append(tens[n // 10])
                n %= 10
            if n > 0:
                ans.append(ones[n])
            return " ".join(ans)
        ans = []
        billion = num // 1_000_000_000
        num %= 1_000_000_000
        million = num // 1_000_000
        num %= 1_000_000
        thousand = num // 1_000
        num %= 1_000
        if billion:
            ans.append(under1000(billion))
            ans.append("Billion")
        if million:
            ans.append(under1000(million))
            ans.append("Million")
        if thousand:
            ans.append(under1000(thousand))
            ans.append("Thousand")
        if num:
            ans.append(under1000(num))
        return " ".join(ans)