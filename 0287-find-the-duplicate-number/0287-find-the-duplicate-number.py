class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        def countGiver(m):
            count = 0
            for i in nums:
                if i <= m:
                    count += 1
            return count
        low = 1
        high = len(nums) - 1
        while low < high:
            middle = low + (high - low)//2
            if countGiver(middle) > middle:
                high = middle 
            else:
                low = middle + 1
        return low
