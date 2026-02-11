class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def checker(d):
            count = 1
            summation = 0
            for i in range(len(nums)):
                if summation + nums[i] > d:
                    count += 1
                    summation = nums[i]
                    continue
                summation += nums[i]
            return count <= k
        low = max(nums)
        high = sum(nums)
        while low < high:
            middle = low + (high - low)//2
            print(middle)
            if checker(middle):
                high = middle
            else:
                low = middle + 1
        return low
