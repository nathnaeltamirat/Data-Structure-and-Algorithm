class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        saver = defaultdict(int)
        l = 0
        res = 0
        def checker(saver):
            count = 0
            max_value = 0
            if len(saver) < 2:
                return True
            for values in saver.values():
                count += values
                max_value = max(max_value,values)
            return count - max_value <= k
        for r in range(len(s)):
            saver[s[r]] += 1    
            while not checker(saver):
                saver[s[l]] -= 1
                if saver[s[l]] == 0:
                    saver.pop(s[l])
                l+=1
            
            res = max(res,r-l+1)
        return res