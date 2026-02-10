class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {letter: i for i, letter in enumerate(s)}
        res = []
        l = 0
        end = -1
        for i in range(len(s)):
            end = max(end,last[s[i]])
            if i == end:
                res.append(i - l + 1)
                l = i+1
        return res