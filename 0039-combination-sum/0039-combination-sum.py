class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(curr,path,curr_sum):
            if curr_sum == target:
                res.append(path[:])
                return
            if curr_sum >= target:
                return
            
            for i in range(curr,len(candidates)):
                path.append(candidates[i])
                curr_sum += candidates[i]
                backtrack(i,path,curr_sum)
                path.pop()
                curr_sum -= candidates[i]
        backtrack(0,[],0)
        return res