class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        def costCalculator(i):
            return abs(ord(s[i]) - ord(t[i]))
        l = 0
        cost = 0
        res = 0
        for r in range(len(s)):
            if costCalculator(r) > maxCost:
                cost = 0
                l = r +1
                continue
            while cost + costCalculator(r) > maxCost:
                cost -= costCalculator(l)
                l+=1
            cost += costCalculator(r)
            res = max(res,r-l+1)
        return res
