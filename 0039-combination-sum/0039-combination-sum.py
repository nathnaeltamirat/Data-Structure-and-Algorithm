class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(path,curr_sum):
            if curr_sum == target:
                t = sorted(path[:])
                if t not in res:
                    res.append(t)
                return
            if curr_sum >= target:
                return
            for i in range(len(candidates)):
                curr_sum += candidates[i]
                path.append(candidates[i])
                backtrack(path,curr_sum)
                curr_sum -= candidates[i]
                path.pop()
        backtrack([],0)
        return res