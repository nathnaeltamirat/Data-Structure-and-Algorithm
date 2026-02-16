class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.n = len(nums)
        def backtrack(curr,k,path):
            if len(path) == k:
                res.append(path[:])
            for i in range(curr,self.n):
                path.append(nums[i])
                backtrack(i+1,k,path)
                path.pop()
       
        
        for i in range(self.n+1):
            backtrack(0,i,[])
        print(res)
        return res
        # for i in range(len(res)):
        #     for j in range(len(res[i])):
        #         res[i][j] = nums[res[i]
        # print(res)

        