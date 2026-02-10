class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = nums[0]
        k = 1

        for i in nums:
            if i != prev:
                nums[k] = i
                k+=1
                prev = i
        return k