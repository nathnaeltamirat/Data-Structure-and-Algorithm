class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] or -nums[i] - 301 == nums[i-1] :
                nums[i] = - nums[i] - 301
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] < -100:
                nums[i] = "_"
        print(nums)
        seeker = pointer = 0
        while seeker < len(nums):
            if nums[seeker] != "_":
                nums[seeker], nums[pointer] = nums[pointer], nums[seeker]
                pointer += 1
            seeker += 1
        
        return pointer
