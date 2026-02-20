class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapify(nums)
        while nums and len(nums) > k:
            heappop(nums)
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums,val)
            return self.nums[0] 
        if  val > self.nums[0]:
            heappop(self.nums)
            heappush(self.nums,val)
        
        return self.nums[0] 
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)