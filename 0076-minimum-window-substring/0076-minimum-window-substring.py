class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = defaultdict(int)

        start = end = 0
        def checker():
            for item in t_count:
                if t_count[item] > s_count[item]:
                    return False
            return True
        valid = False
        l = 0
        res = float('inf')
        for r in range(len(s)):
            s_count[s[r]] += 1
            if not valid:
                if checker():
                    valid = True
            while valid and s_count[s[l]] > t_count[s[l]]:
                s_count[s[l]]-=1
                l+=1
            
            if valid and (r-l+1) < res:
                res = r-l+1
                start = l
                end = r
        return s[start:end+1] if res != float('inf') else ""