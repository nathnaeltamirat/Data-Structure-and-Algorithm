class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        res = 0
        l, r = 0, len(people) - 1
        while l <= r:
            if  people[l] + people[r] <= limit:
                r -= 1
                l += 1
            else:
                
                r -= 1
            res += 1
        return res
            
  