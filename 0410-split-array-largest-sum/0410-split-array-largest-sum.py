class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def checker(val):
            curr_k = 1
            curr_val = 0
            for i in range(len(nums)):
                if curr_val + nums[i] > val:
                    curr_val = nums[i]
                    curr_k += 1
                else:
                    curr_val += nums[i]
            return curr_k <= k
            
        low = max(nums)
        high = sum(nums)

        while low <= high:
            medium = low + (high - low)//2

            if checker(medium):
                high = medium - 1
            else:
                low = medium + 1
        return low