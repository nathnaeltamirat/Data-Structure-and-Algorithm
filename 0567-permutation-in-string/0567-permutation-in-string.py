class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        counts2 = defaultdict(int)
        if len(s1) > len(s2):
            return False
        l = 0
        k = len(s1)
        for r in range(k):
            counts2[s2[r]] += 1
        if counts2 == count:
            return True
        for r in range(k,len(s2)):
            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                counts2.pop(s2[l])
            counts2[s2[r]] += 1
 
            if counts2 == count:
                return True
            l+=1
        return False