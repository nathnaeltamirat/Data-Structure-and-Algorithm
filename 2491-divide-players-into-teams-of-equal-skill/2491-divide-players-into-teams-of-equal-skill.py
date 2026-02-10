class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res  = 0
        l , r = 0, len(skill) - 1
        checker = set()
        while l < r:
            c_skill = skill[l] * skill[r]
            checker.add(skill[l] + skill[r])
            res += c_skill
            l += 1
            r -= 1
        
        if len(checker) == 1:
            return res
        return -1 