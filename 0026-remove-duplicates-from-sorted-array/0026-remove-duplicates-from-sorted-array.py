class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        prev = nums[0]
        for i in nums:
            if prev != i:
                nums[k] = i
                k+=1
                prev = i
        return k
