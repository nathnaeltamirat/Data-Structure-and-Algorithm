class Solution:
    def minWindow(self, s: str, t: str) -> str:
        valid = False
        l = 0
        t_count = Counter(t)
        s_count = defaultdict(int)
        res = float('inf')
        def checker():
            for i in t_count:
                # print(t_count[i],s_count[i])
                if t_count[i] > s_count[i]:
                    return False
            return True
        start = end = 0
        for r in range(len(s)):
            s_count[s[r]] += 1
            # print(s_count,t_count)
            if not valid:
                if checker():
                    valid = True
            while valid and s_count[s[l]] > t_count[s[l]]:
                s_count[s[l]] -= 1
                l += 1
            if valid:
                if r -l + 1 < res:
                    res = r-l+1

                    start , end = l, r
        return s[start:end+1] if res != float('inf') else ""
            