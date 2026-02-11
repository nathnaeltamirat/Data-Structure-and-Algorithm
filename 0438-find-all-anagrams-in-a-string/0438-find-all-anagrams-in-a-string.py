class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        sliding = defaultdict(int)
        res = []
        l = 0
        for r in range(len(s)):
            if s[r] not in count:
                sliding.clear()
                l = r+1
                continue
            while sliding[s[r]] == count[s[r]]:
                sliding[s[l]]-=1
            
                if sliding[s[l]] == 0:
                    sliding.pop(s[l])
                l+=1
            sliding[s[r]] += 1
            if sliding == count:
                res.append(l)
        return res
