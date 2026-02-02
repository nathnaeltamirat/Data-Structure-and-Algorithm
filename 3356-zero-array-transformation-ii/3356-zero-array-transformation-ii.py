class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def checker(k):
            new_nums = [0] * len(nums)
            for i in range(0,k):
                l , r, val = queries[i]
                new_nums[l] += val
                if r != len(new_nums) - 1:
                    new_nums[r+1]-= val
            
            for i in range(1,len(new_nums)):
                new_nums[i] += new_nums[i-1]
            
            for i in range(len(nums)):
                if nums[i] > new_nums[i]:
                    return False
            return True
        low = 0
        high = len(queries)

        while low <= high:
            middle = low + (high - low)//2
            if checker(middle):
                print(middle)
                high = middle - 1
            else:
                low = middle + 1
        return low if low <=len(queries) else -1


