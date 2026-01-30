class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def checker(val):
            curr_k = 1
            curr_val = 0
            for i in nums:
                if curr_val + i > val:
                    curr_val = i
                    curr_k += 1
                else:
                    curr_val += i
            return curr_k <= k

        low = max(nums)
        high =  sum(nums)

        while low < high:
            middle = low + (high - low)//2
            if checker(middle):
                high = middle
            else:
                low = middle + 1
        return low